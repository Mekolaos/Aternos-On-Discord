import discord
import os
from lxml import html
import requests
from connect_and_launch import start_server
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == '-Jackadit launch_server':
        if get_status() == "Offline":
            await message.channel.send("Launching the server boss !")
            await start_server()
        else:
            await message.channel.send("The server is already Online")
    if message.content == '-Jackadit server_status':
        status = get_status()
        await message.channel.send("The server is {}".format(status))
    if message.content == '-Jackadit players':
        players = get_number_of_players()
        await message.channel.send("There are {} players on the server".format(players))
    if message.content == '-Jackadit stop_server':
        await message.channel.send("Mazal ma temchi")

def get_status():
    page = requests.get('https://jackadit.aternos.me')
    tree = html.fromstring(page.content)
    status = tree.xpath('/html/body/div/div[3]/div/div/div[1]/span/text()')
    return status[0]
def get_number_of_players():
    page = requests.get('https://jackadit.aternos.me')
    tree = html.fromstring(page.content)
    status = tree.xpath('/html/body/div/div[4]/div/div/div/span[1]/text()')
    return status[0]

    
    

client.run(BOT_TOKEN)
