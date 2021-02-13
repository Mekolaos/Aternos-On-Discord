from discord import Embed
from connect_and_launch import get_server_info


def server_info_embed():
    """ Generates embed object for server info"""
    ip, status, players, software, version = get_server_info()
    text = f"**IP:** {ip} \n" \
           f"**Status:** {status} \n" \
           f"**Players:** {players} \n" \
           f"**Version:** {software} {version}"
    embed = Embed()
    embed.add_field(name="Server Info", value=text, inline=False)
    return embed


def help_embed():
    """ Generates embed object for help command"""
    embed = Embed(title="Help")
    embed.add_field(name="--launch server",
                    value="Launches the server",
                    inline=False)
    embed.add_field(name="--server status",
                    value="Gets the server status",
                    inline=False)
    embed.add_field(name="--server info",
                    value="Gets the server info",
                    inline=False)
    embed.add_field(name="--players",
                    value="Gets the number of players",
                    inline=False)
    embed.add_field(name="--stop server",
                    value="Stops the server",
                    inline=False)
    embed.add_field(name="--crash",
                    value="Shuts down the bot",
                    inline=False)
    embed.add_field(name="--help",
                    value="Displays this message",
                    inline=False)
    return embed
