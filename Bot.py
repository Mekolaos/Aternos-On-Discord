import datetime
import time

import Settings
import discord
import connect_and_launch
import colorama
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
    connect_and_launch.connect_account()

    #Start both thingies
    reloadBrowser.start()
    updateStatus.start()


@bot.command()
async def launch(ctx):
    status = connect_and_launch.get_status()

    if status == "Offline":
        await ctx.send("Starting the server...")
        connect_and_launch.start_server()

        author = ctx.author

        print("[" + datetime.datetime.now().strftime("%H:%M:%S") + "]" + colorama.Fore.GREEN + "Server launched by " + colorama.Fore.CYAN + author.name, author.discriminator + colorama.Style.RESET_ALL)

        while True:
            time.sleep(5)
            if connect_and_launch.get_status() == "Online":
                await ctx.send(f"{author.mention}, the server has started!")
                break


    elif connect_and_launch.get_status() == "Online":
        await ctx.send("The server is already online.")

    else:
        await ctx.send("Could not start the server. Reason: server is " + connect_and_launch.get_status())


@bot.command()
async def status(ctx):
    await ctx.send(embed=server_info_embed())


@bot.command()
async def help(ctx):
    await ctx.send(embed=help_embed())




#T A S K S

@tasks.loop(seconds=15.0)
async def updateStatus():
    server_status = connect_and_launch.get_status()
    if server_status == "Online":
        text = f"Server: Online | " \
               f"{len(connect_and_launch.get_players())} | " \
               f"--help"

    else:
        text = f"Server: {connect_and_launch.get_status()} | " \
               f"--help"

    activity = discord.Activity(type=discord.ActivityType.watching, name=text)
    await bot.change_presence(activity=activity)





@tasks.loop(hours=1.0)
async def reloadBrowser():
    connect_and_launch.refreshBrowser()

def print_out(out, color):
    print("")
    print("[" + datetime.datetime.now().strftime("%H:%M:%S") + "]" + color, out, colorama.Style.RESET_ALL)



#Run bot
bot.run(Settings.Token)
