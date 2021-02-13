import discord
import os
import sys
import asyncio
from dotenv import load_dotenv
from discord.ext import tasks, commands
from Configure import launch_config
from connect_and_launch import get_server_info, get_status, \
    get_number_of_players, get_version, get_software, get_ip, get_tps
from connect_and_launch import connect_account, quitBrowser
from connect_and_launch import start_server, stop_server
from embeds import server_info_embed, help_embed

# setup environment vars if .env doesn't exist
if not os.path.exists(os.path.relpath(".env")):
    launch_config()
    sys.exit()

# load environment vars
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# bot settings
intents = discord.Intents.default()
allowed_mentions = discord.AllowedMentions(everyone=False, roles=False,
                                           users=True)
description = 'A simple tool to serve your own discord bot so you can ' \
              'manage an Aternos server from discord.'
bot = discord.ext.commands.Bot(command_prefix='--', intents=intents,
                               allowed_mentions=allowed_mentions,
                               description=description,
                               case_insensitive=True,
                               help_command=None)


@bot.event
async def on_ready():
    text = "Logging into Aternos... | --help"
    await bot.change_presence(activity=discord.Game(name=text))

    connect_account()  # logs into aternos
    print(f'The bot is logged in as {bot.user}')
    await asyncio.sleep(2)
    serverStatus.start()  # starts the presence update loop


@bot.command()
async def launch(ctx):
    """ Launches the Minecraft Server"""
    server_status = get_status()

    if server_status == "Offline":
        await ctx.send("Starting the server...")
        await start_server()

        # if pinging a person, server will ping them when launching
        # else ping the the user who sent the command on launch
        if len(ctx.message.mentions) == 0:
            author = ctx.author
        else:
            author = ctx.message.mentions[0]

        # loops until server has started and pings person who launched
        while True:
            await asyncio.sleep(5)
            if get_status() == "Online":
                await ctx.send(f"{author.mention}, the server has started!")
                break

    elif server_status == "Online":
        await ctx.send("The server is already Online.")

    elif server_status == "Starting ..." or server_status == "Loading ...":
        await ctx.send("The server is already starting...")

    elif server_status == "Stopping ..." or server_status == "Saving ...":
        await ctx.send("The server is stopping. Please wait.")

    else:
        text = "An error occurred. Either the status server is not " \
               "responding or you didn't set the server name " \
               "correctly.\n\nTrying to launch the server anyways."
        await ctx.send(text)
        await start_server()


@bot.command()
async def status(ctx):
    await ctx.send(f"The server is {get_status()}")


@bot.command()
async def players(ctx):
    await ctx.send(f"There are {get_number_of_players()} players online.")


@bot.command()
async def info(ctx):
    await ctx.send(embed=server_info_embed())


@bot.command()
async def stop(ctx):
    await ctx.send("Stopping the server...")
    server_status = get_status()

    if server_status != 'Stopping ...' or server_status != 'Saving ...' or \
            server_status != 'Offline':
        await stop_server()

    else:
        await ctx.send("The server is already Offline.")


@bot.command()
async def help(ctx):
    """ Help Command"""
    await ctx.send(embed=help_embed())


@tasks.loop(seconds=5.0)
async def serverStatus():
    server_status = get_status()
    text = None
    if server_status == "Online":
        text = f"Server: {get_status()} | " \
               f"Players: {get_number_of_players()} | " \
               f"TPS: {get_tps()} | " \
               f"--help"
    else:
        text = f"Server: {get_status()} | " \
               f"{get_ip()} | " \
               f"--help"
    activity = discord.Activity(type=discord.ActivityType.watching, name=text)
    await bot.change_presence(activity=activity)


bot.run(BOT_TOKEN)
