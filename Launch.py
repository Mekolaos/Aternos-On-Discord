import time

import Settings
import discord
import Functions
from discord.ext import tasks, commands

from Embeds import server_info_embed, help_embed

bot = discord.ext.commands.Bot(command_prefix='--',
                               description=Settings.description,
                               case_insensitive=True,
                               help_command=None)

@bot.event
async def on_ready():
    #Set basic status
    status = "Please wait..."

    await bot.change_presence(activity=discord.Game(name=status))

    #Login to aternos here
    Functions.connect_account()

    #Start both thingies
    reloadBrowser.start()
    updateStatus.start()


@bot.command()
async def launch(ctx):
    status = Functions.get_status()

    if status == "Offline":
        await ctx.send("Starting the server...")
        Functions.start_server()

        author = ctx.author

        print("Server launched by " + author.name, author.discriminator)

        while True:
            time.sleep(5)
            if Functions.get_status() == "Online":
                await ctx.send(f"{author.mention}, the server has started!")
                break


    elif Functions.get_status() == "Online":
        await ctx.send("The server is already online.")

    else:
        await ctx.send("Could not start the server. Reason: server is " + Functions.get_status())


@bot.command()
async def status(ctx):
    await ctx.send(embed=server_info_embed())


@bot.command()
async def help(ctx):
    await ctx.send(embed=help_embed())




#T A S K S

@tasks.loop(seconds=15.0)
async def updateStatus():
    server_status = Functions.get_status()
    if server_status == "Online":
        text = f"Server: Online | " \
               f"{len(Functions.get_players())} | " \
               f"--help"

    else:
        text = f"Server: {Functions.get_status()} | " \
               f"--help"

    activity = discord.Activity(type=discord.ActivityType.watching, name=text)
    await bot.change_presence(activity=activity)


@tasks.loop(minutes=5)
async def tryfixes():
    #also try
    Functions.fix_serverlist()




@tasks.loop(hours=1.0)
async def reloadBrowser():
    Functions.refreshBrowser()




#Run bot
bot.run(Settings.Token)
