import discord
from discord.ext import commands
from discord import Game

bot = commands.Bot(command_prefix= "!")

@bot.event
async def on_ready():
    print("Status is online. Made by MivanOfficial💓")
    print("Discord Username: {}".format(bot.user.name))
    print("Discord UserID: {}".format(bot.user.id))
    await bot.change_presence(activity=Game(name="💓Ваш статус", type="")) 
    #прочитайте файл statuses.json там написаны все статусы.

bot.run("ваш токен", bot=false)
