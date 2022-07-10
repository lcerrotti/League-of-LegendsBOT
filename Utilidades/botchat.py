from riotwatcher import LolWatcher
from riotwatcher import ApiError
import os
from urllib import response
from dotenv import load_dotenv
from discord.ext import commands
from funciones import *
import pandas as pd



#Cargamos el archivo .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#Definimos el Bot
bot = commands.Bot(command_prefix="!") # Prefijo de comando

@bot.command(name="mastery")
async def mastery(ctx,my_region,summoner_name,info):
    response = await mayor_maestry(ctx,my_region,summoner_name,info)
    await ctx.send(response)

@bot.command(name="lot")
async def lot(ctx,my_region,summoner_name,match_num):
    response = await what_is_my_team(ctx,my_region,summoner_name,int(match_num))
    await ctx.send(f"El equipo azul estaba conformado por **{response[0][0]}** , **{response[0][1]}** , **{response[0][2]}** , **{response[0][3]}** , **{response[0][4]}** \n Y el equipo rojo por **{response[1][0]}** , **{response[1][1]}** , **{response[1][2]}** , **{response[1][3]}** , **{response[1][4]}**")


@bot.command(name="tb")
async def table(ctx):
    # Define a dictionary containing employee data
    data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
            'Age':[27, 24, 22, 32],
            'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
            'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
    
    # Convert the dictionary into DataFrame 
    df = pd.DataFrame(data)
    
    # select two columns
    response =  df[['Name', 'Qualification',"Age","Address"]]
    await ctx.send(response)
    




bot.run(TOKEN)