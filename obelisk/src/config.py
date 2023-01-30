import discord
from discord.ext import commands
import json

config = json.load(open("config.json"))

PREFIX = config["prefix"]
TOKEN = open("TOKEN").read()
DCOLOR = discord.Colour.from_str(config["dev_color"])
BCOLOR = discord.Colour.from_str(config["bot_color"])

BOT = commands.Bot(command_prefix=PREFIX,
                   intents=discord.Intents.all())
CLIENT = discord.Client(intents=discord.Intents.all())

help_text = """
`help` - displays the help menu
`test` - displays a test message
`dev` - sends a developer debug embed
"""