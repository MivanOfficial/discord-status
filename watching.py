import discord
import config
from discord.ext import commands
from discord import Game

bot = commands.Bot(command_prefix= "!")

@bot.event
async def on_ready():
    print("Status is online. Made by MivanOfficial💓")
    print("Discord Username: {}".format(bot.user.name))
    print("Discord UserID: {}".format(bot.user.id))
    
    statusTEXT = config.statusTEXT
    activity = discord.Activity(name=statusTEXT, type=discord.ActivityType.watching)
    await bot.change_presence(status=discord.Status.online, activity=activity)

bot.run(config.token, bot=False)
