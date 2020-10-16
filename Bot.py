import discord
from discord.ext import commands
import os
from Configure import launch_config
from dotenv import load_dotenv
import json
from connect_and_launch import start_server, get_status, stop_server

if not os.path.exists(os.path.relpath(".env")):
    launch_config()

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
SERVER_STATUS_URI = "http://" + os.getenv("SERVER_STATUS_URI")
HEADER = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.125"}

client = discord.Client()

@client.event
async def on_ready():
    print('The bot is logged in as {0.user}'.format(client))

    

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    
    if message.content.startswith('--'):

        if message.content == '--launch server':

            await message.channel.send("Launching Server...")
            status = get_status()

            if status == "Offline":
                await start_server

            elif status == "Online":
                await message.channel.send("The server is already Online")

            else :
                await message.channel.send("An error occured. Either the status server is not responding, or you didn't set the server name correctly.\nTrying to launch server anyway.")
                await start_server

        elif message.content == '--server status':
            await message.channel.send("Getting status...")
            status = get_status()
            await message.channel.send("The server is {}".format(status))

        elif message.content == '--players':
            await message.channel.send("Getting players...")
            try:
                players = get_number_of_players()
            except:
                await message.channel.send("There are no players on the server")
            else: 
                await message.channel.send("There are {} players on the server".format(players))

        elif message.content == '--stop server':
            await message.channel.send("Stopping the server.")
            await stop_server

        elif message.content == '--help': 
            embed = discord.Embed(title="Help")
            embed.add_field(name="--launch server", value="Launches the server", inline=False)
            embed.add_field(name="--server status", value="Gets the server status", inline=False)
            embed.add_field(name="--players", value="Gets the number of players", inline=False)
            embed.add_field(name="--stop server", value="Stops the server", inline=False)
            embed.add_field(name="--help", value="Displays this message", inline=False)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send("Unknown command, use --help to see a list of all availiable commands")
    

client.run(BOT_TOKEN)
