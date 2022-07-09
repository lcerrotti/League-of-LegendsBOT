from asyncore import read
from numpy import append
from riotwatcher import LolWatcher
from riotwatcher import ApiError
import os
from urllib import response
from dotenv import load_dotenv
from discord.ext import commands
import json

# Riot API Key
key = 'RGAPI-e38e2357-669b-45d6-8f64-0cbef4ab3ca1'
api_key = key
watcher = LolWatcher(api_key)

def mayor_maestry(my_region,summoner_name):

  # Get summoner data
  me = watcher.summoner.by_name(my_region, str(summoner_name))
  
  #Obtengo una lista con dicccionarios con la informacion de los campeones.
  total_maestry = watcher.champion_mastery.by_summoner(my_region,me['id']) # Get masteries data
  
  # Creo Listas que guarden lo que necesitare para crear un dataframe.
  first3_mastery_champs = []
  first3_mastery_champs_names = []
  first3_mastery_points = []
  first3_mastery_champslvl = []


  for i in range(3):
    first3_mastery_champslvl.append(total_maestry[i]['championLevel'])
    first3_mastery_points.append(total_maestry[i]['championPoints'])
    first3_mastery_champs.append(total_maestry[i]['championId'])
    
   
  print(first3_mastery_champs)

  # Buscar en champions.json el id de los campeones y obtener el nombre del campeon en total_maestry

  with open('D:\Python\League-of-LegendsBOT\Utilidades\__pycache__\champion.json','r', encoding='utf-8') as file:   
     data = json.load(file) 
     data_champs_all = data['data']
     for key in data_champs_all:
         if data_champs_all[key]['key'] == first3_mastery_champs[0]:
            first3_mastery_champs_names.append(data_champs_all[key]['name'])
         if data_champs_all[key]['key'] == first3_mastery_champs[1]:
            first3_mastery_champs_names.append(data_champs_all[key]['name'])
         if data_champs_all[key]['key'] == first3_mastery_champs[2]:
            first3_mastery_champs_names.append(data_champs_all[key]['name'])     


             

  print(first3_mastery_champs_names)


 

  



            
 


mayor_maestry("la2","XxSoul MasterxX")


#   if info == "Maestry":
#      return first3_mastery_points
#   elif info == "Level":     
#      return first3_mastery_champslvl
#   elif info == "Name":
#      #return lista_de_champs
#   elif info == "All":
#      return total_maestry
#   elif info == "Allstr":
#      #return f"Tus personajes con maestria mas alta son: {#champ_name1}, con {#first3_mastery_points[0]} ,{#champ_name2} con {#first3_mastery_points[1]} y {#champ_name3} con {#first3_mastery_points[2]} \n y sus niveles son {#first3_mastery_champslvl} respectivamente."
