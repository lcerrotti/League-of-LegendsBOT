import os
from urllib import response
from dotenv import load_dotenv
from discord.ext import commands
from Utilidades.funciones import mayor_maestry

#Cargamos el archivo .env
#load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')


## https://riot-watcher.readthedocs.io/en/latest/riotwatcher/LeagueOfLegends/index.html
# Requiere un servidor , un nombre de invocador y una clave para operar (determina el resutlado de la funcion) (Maestry, Level, Name , All , Allstr)                                                                                                                                                                                                                                                                                                                                                                                                                                        
#print(mayor_maestry("la2" ,"XxSoul MasterxX", "Allstr"))


#bot = commands.Bot(command_prefix="-") # Prefijo de comando


#@bot.command(name="suma")
#async def sumar(ctx, num1, num2):
    #response = int(num1) + int(num2)
    #await ctx.send(response)
    
#bot.run(TOKEN)