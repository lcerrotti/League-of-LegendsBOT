from riotwatcher import LolWatcher
from riotwatcher import ApiError
import os
from urllib import response
from dotenv import load_dotenv
from discord.ext import commands
import json


# Riot API Key
key = 'RGAPI-714088e7-590f-42cd-8a89-ab750a7c9b80'
api_key = key
watcher = LolWatcher(api_key)




# Obtengo la informacion de una partida por personaje.
#servidor , summoner_name, match_num, *args (si se agrega un parametro mas, se retorna solo ese parametro)
#print(participants_stats_inMatch("la2","XxSoul MasterxX",0,"XxSoul MasterxX"))
def participants_stats_inMatch(my_region, summoner_name, match_num, *args):

  argssumm = args[0]

  # Obtengo el puuid del summoner para separarlo en una variable.
  me = watcher.summoner.by_name(my_region, summoner_name)
  puuid =  me['puuid']

  # Otengo un Metadata con toda la informacion de la partida.
  matches20 = watcher.match.matchlist_by_puuid(my_region, puuid)

  # Desestructurando un Metadata de una partida.
  match_selected = watcher.match.by_id(my_region, matches20[match_num]) # Obtengo el match con el ID mas reciente. (MODIFICANDO EL 0 ELIJO LA PROXIMA PARTIDA)


  # Declarando participantes de la partida.
  participants = match_selected["info"]["participants"]


  if args:
     for participant in participants:
         if participant["summonerName"] == argssumm:
            if len(args) == 1:
               return participant
            else:
             return participant[args[1]]
     else:
       return None


# Obtengo la informacion de los campeones con mayor maestria (Primeros 3)
# servidor, invocador, parametro
# mayor_maestry("la2","XxSoul MasterxX","Allstr")

async def mayor_maestry(ctx,my_region,summoner_name,info):

    
  # Get summoner data
  me = watcher.summoner.by_name(my_region, str(summoner_name))
  
  #Obtengo una lista con dicccionarios con la informacion de los campeones.
  total_maestry = watcher.champion_mastery.by_summoner(my_region,me['id']) # Get masteries data


  # Creo Listas que guarden lo que necesitare para crear un dataframe.
  first3_mastery_champs = [] #Esta lista se genera a partir de los resultados en total_maestry
  first3_mastery_champs_names = []
  first3_mastery_points = []
  first3_mastery_champslvl = []

  keychamplist = [] # lista para guardar nuevos keys de los campeones
  valueschamplist = [] # lista para guardar nuevos values de los campeones
  

  for i in range(3):
    first3_mastery_champslvl.append(total_maestry[i]['championLevel'])
    first3_mastery_points.append(total_maestry[i]['championPoints'])
    first3_mastery_champs.append(total_maestry[i]['championId'])
    

  # Buscar en champions.json el id de los campeones y obtener el nombre del campeon en total_maestry

  with open('Utilidades\ArchivosExternos\champion.json','r', encoding='utf-8') as file:   
     data = json.load(file) 
     data_champs_all = data['data']
     #print(data_champs_all["Aatrox"])
     for key in data_champs_all:
         keychamplist.append(data_champs_all[key]["id"])  
         valueschamplist.append(data_champs_all[key]["key"])


   # Armar un dict con las listas keychamplist y valueschamplist
  dict_from_list = dict(zip(keychamplist, valueschamplist))


  for key in dict_from_list:
      if int(dict_from_list[key]) == first3_mastery_champs[0]:
             first3_mastery_champs_names.append(key)
      elif int(dict_from_list[key]) == first3_mastery_champs[1]:
             first3_mastery_champs_names.append(key)
      elif int(dict_from_list[key]) == first3_mastery_champs[2]:
             first3_mastery_champs_names.append(key)

  if info == "Maestry":
     response = first3_mastery_points
     await ctx.send(response)
     #return first3_mastery_points
  elif info == "Level":
     response = first3_mastery_champslvl
     await ctx.send(response)
     #return first3_mastery_champslvl
  elif info == "Name":
     response = first3_mastery_champs_names
     await ctx.send(response)
     #return lista_de_champs
  elif info == "All":
     response = [first3_mastery_points, first3_mastery_champslvl, first3_mastery_champs_names]
     await ctx.send(response)
     #return total_maestry
  elif info == "Allstr":
     response = f"Tus personajes con maestria mas alta son: {first3_mastery_champs_names[0]}, con {first3_mastery_points[0]} ,{first3_mastery_champs_names[1]} con {first3_mastery_points[1]} y {first3_mastery_champs_names[2]} con {first3_mastery_points[2]} \n y sus niveles son {first3_mastery_champslvl} respectivamente."
     await ctx.send(response)
     #return f"Tus personajes con maestria mas alta son: {champ_name1}, con {first3_mastery_points[0]} ,{champ_name2} con {first3_mastery_points[1]} y {champ_name3} con {first3_mastery_points[2]} \n y sus niveles son {first3_mastery_champslvl} respectivamente."



#Obtengo las ultimas 10 partidas de un campeon.
#servidor,invocador, (sin args ultimas 20 partidas con args una partida en especifico)
#print(list_of_matchs("la2","XxSoul MasterxX"))
def list_of_matchs(my_region,summoner_name,*args):

        # Obtengo el puuid del summoner para separarlo en una variable.
        me = watcher.summoner.by_name(my_region, summoner_name)
        puuid =  me['puuid']

        # Otengo un Metadata con toda la informacion de la partida.
        matches20 = watcher.match.matchlist_by_puuid(my_region, puuid)


        # Desestructurando un Metadata de una partida.
        if args:
         return matches20[args[0]] # Obtengo el match con el ID mas reciente. (MODIFICANDO EL 0 ELIJO LA PROXIMA PARTIDA)
        else:
         return matches20


#Obtener ganadores y perdedores.
# servidor, invocador, numero de partida,dependiendo el color del team , si gana devuelve true , si pierde devuelve false.
#print(whowin_in("la2","XxSoul MasterxX",0,"red"))
def whowin_in(my_region,summoner_name,match_num,team_color):

  # Obtengo el puuid del summoner para separarlo en una variable.
  me = watcher.summoner.by_name(my_region, summoner_name)
  puuid =  me['puuid']

  # Otengo un Metadata con toda la informacion de la partida.
  matches20 = watcher.match.matchlist_by_puuid(my_region, puuid)

  # Desestructurando un Metadata de una partida.
  match_selected = watcher.match.by_id(my_region, matches20[match_num]) # Obtengo el match con el ID mas reciente. (MODIFICANDO EL 0 ELIJO LA PROXIMA PARTIDA)

  # Declarando participantes de la partida.
  teams = match_selected["info"]["teams"]
  team_blue = teams[0]
  team_red = teams[1]

  if team_color == "blue":
     if team_blue["win"] == True:
         return True
     else:
         return False

  if team_color == "red":
     if team_red["win"] == True:
         return True
     else:
         return False


# Obtener equipos
# servidor, invocador, numero de la partida. (devuelve 2 listas con los nombres de los participantes de cada equipo)
#blue_team = what_is_my_team("la2","XxSoul MasterxX",0)[0]
#print(blue_team)
#red_team = what_is_my_team("la2","XxSoul MasterxX",0)[1]
#print(red_team)
async def what_is_my_team(ctx,my_region, summoner_name, match_num):

  # Obtengo el puuid del summoner para separarlo en una variable.
  me = watcher.summoner.by_name(my_region, summoner_name)
  puuid =  me['puuid']

  # Otengo un Metadata con toda la informacion de la partida.
  matches20 = watcher.match.matchlist_by_puuid(my_region, puuid)

  # Desestructurando un Metadata de una partida.
  match_selected = watcher.match.by_id(my_region, matches20[match_num]) # Obtengo el match con el ID mas reciente. (MODIFICANDO EL 0 ELIJO LA PROXIMA PARTIDA)

  # Declarando participantes de la partida.
  participants = match_selected["info"]["participants"]
  blue_team = []
  red_team = []

  for player in participants:
     if player["teamId"] == 100:
        blue_team.append(player["summonerName"])
   
  for player in participants:
     if player["teamId"] == 200:
        red_team.append(player["summonerName"])
   
  return blue_team, red_team


def what_is_my_team4class(my_region, summoner_name, match_num):

  # Obtengo el puuid del summoner para separarlo en una variable.
  me = watcher.summoner.by_name(my_region, summoner_name)
  puuid =  me['puuid']

  # Otengo un Metadata con toda la informacion de la partida.
  matches20 = watcher.match.matchlist_by_puuid(my_region, puuid)

  # Desestructurando un Metadata de una partida.
  match_selected = watcher.match.by_id(my_region, matches20[match_num]) # Obtengo el match con el ID mas reciente. (MODIFICANDO EL 0 ELIJO LA PROXIMA PARTIDA)

  # Declarando participantes de la partida.
  participants = match_selected["info"]["participants"]
  blue_team = []
  red_team = []

  for player in participants:
     if player["teamId"] == 100:
        blue_team.append(player["summonerName"])
   
  for player in participants:
     if player["teamId"] == 200:
        red_team.append(player["summonerName"])
   
  return blue_team, red_team



def gamemode(my_region, summoner_name, match_num):
   # Obtengo el puuid del summoner para separarlo en una variable.
  me = watcher.summoner.by_name(my_region, summoner_name)
  puuid =  me['puuid']

  # Otengo un Metadata con toda la informacion de la partida.
  matches20 = watcher.match.matchlist_by_puuid(my_region, puuid)

  # Desestructurando un Metadata de una partida.
  match_selected = watcher.match.by_id(my_region, matches20[match_num]) # Obtengo el match con el ID mas reciente. (MODIFICANDO EL 0 ELIJO LA PROXIMA PARTIDA)


  # Declarando participantes de la partida.
  gamemode = match_selected["info"]["gameMode"]


  return gamemode


def gameDuration(my_region, summoner_name, match_num):
   # Obtengo el puuid del summoner para separarlo en una variable.
  me = watcher.summoner.by_name(my_region, summoner_name)
  puuid =  me['puuid']

  # Otengo un Metadata con toda la informacion de la partida.
  matches20 = watcher.match.matchlist_by_puuid(my_region, puuid)

  # Desestructurando un Metadata de una partida.
  match_selected = watcher.match.by_id(my_region, matches20[match_num]) # Obtengo el match con el ID mas reciente. (MODIFICANDO EL 0 ELIJO LA PROXIMA PARTIDA)


  # Declarando participantes de la partida.
  gameDuration = match_selected["info"]["gameDuration"]


  return gameDuration























