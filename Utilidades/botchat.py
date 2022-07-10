from riotwatcher import LolWatcher
from riotwatcher import ApiError
import os
from urllib import response
from dotenv import load_dotenv
from discord.ext import commands
from funciones import *
import pandas as pd
import df2img
import discord


#Cargamos el archivo .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#Definimos el Bot
bot = commands.Bot(command_prefix="!") # Prefijo de comando

@bot.command(name="h")
async def help(ctx):
    response = "**!h:** *Muestra la lista de comandos*\n**!mastery (servidor) (Nombre de Invocador) (Allstr):** *Muestra las primeras 3 maestrias (si el nombre tiene espacio encerrarlo entre comillas)*\n**!lot (servidor) (Nombre de Invocador) (Numero de Partida):** *Muestra la lista de players de una partida (si el nombre tiene espacio encerrarlo entre comillas)*\n**!tb:** *Muestra la tabla de campeones*" 
    await ctx.send(response)

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
    df = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
            'Age':[27, 24, 22, 32],
            'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
            'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
    
    # Convert the dictionary into DataFrame 
    df = pd.DataFrame(df)
    
    # select two columns
    print(df[['Name', 'Qualification',"Age","Address"]])



    fig = df2img.plot_dataframe(
        df,
        # title=dict(
        #     font_color="darkred",
        #     font_family="Times New Roman",
        #     font_size=16,
        #     text="This is a title",
        # ),
        tbl_header=dict(
            align="right",
            fill_color="#327778",
            font_color="white",
            font_size=10,
            line_color="darkslategray",
        ),
        tbl_cells=dict(
            align="right",
            line_color="darkslategray",
        ),
        row_fill_color=("#AFFEFF", "#13D1D4"),
        fig_size=(480, 120),
    )

    df2img.save_dataframe(fig=fig, filename="plot.png")
    await ctx.send(file=discord.File('plot.png'))
    




bot.run(TOKEN)