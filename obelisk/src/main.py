import discord
from discord.ext import commands
import asyncio

from src.config import *
cfig = config # initial config creation

BOT.remove_command('help')

class CommandErrorHandler(commands.Cog):
    def __init__(self, bot) : self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error) : print(error)


@BOT.event
async def on_member_join(mbr):
    print(mbr.name, "has joined")
    join_channel = discord.utils.get(mbr.guild.channels, id=1066980676991193168)
    await join_channel.send(
        content=mbr.mention,
        embed=discord.Embed(
            title = "Welcome!",
            description = cfig["welcome_message"],
            color = BCOLOR
        ))

@BOT.command()
async def dev(ctx):
    if ctx.author.id not in cfig["authorized_users"] : return
    await ctx.send(embed = discord.Embed(
        title = "Developer Debug Window",
        description = "This is just an embed test.",
        color = DCOLOR
    ))

@BOT.command()
async def test(ctx):
    if ctx.author.id not in cfig["authorized_users"] : return
    if ctx.channel.name == "the-lab" : await ctx.send(content = "Test Completed", embed = discord.Embed(
            title = "Test Completed",
            color = DCOLOR
    ))

@BOT.command()
async def help(ctx):
    await ctx.send(embed = discord.Embed(
        title = "Help",
        description = help_text,
        color = BCOLOR
    ))
    
@BOT.command()
async def reload(ctx):
    global cfig, DCOLOR, BCOLOR, help_text
    if ctx.author.id in cfig["authorized_users"]:
        config = json.load(open("config.json"))
        cfig = config
        DCOLOR = discord.Colour.from_str(config["dev_color"])
        BCOLOR = discord.Colour.from_str(config["bot_color"])
        await ctx.send("Successfully reloaded the configuration files.")

@BOT.command()
async def config(ctx):
    if ctx.author.id not in cfig["authorized_users"] : return
    c = open("config.json").read()
    await ctx.send(content=f'```json\n{c}\n```')


@BOT.event
async def on_ready() : print("OBELISK READY")

def main():

    loop = asyncio.get_event_loop()
    loop.create_task(BOT.start(TOKEN))
    loop.create_task(CLIENT.start(TOKEN))

    try : loop.run_forever()
    except:
        print("Exiting OBELISK")
        quit()
