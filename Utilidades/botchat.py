import imp
from riotwatcher import LolWatcher
from riotwatcher import ApiError
import os
from urllib import response
from dotenv import load_dotenv
from discord.ext import commands
from funciones import *



#Cargamos el archivo .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#Definimos el Bot
bot = commands.Bot(command_prefix="!") # Prefijo de comando

@bot.command(name="mastery")
async def mastery(ctx,my_region,summoner_name,info):
    response = await mayor_maestry(ctx,my_region,summoner_name,info)
    await ctx.send(response)














bot.run(TOKEN)