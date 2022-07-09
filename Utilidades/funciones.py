from riotwatcher import LolWatcher
from riotwatcher import ApiError
import os
from urllib import response
from dotenv import load_dotenv
from discord.ext import commands


# Riot API Key
key = 'RGAPI-44e1e2a7-d60a-4d9a-88eb-b81a2da646b4'
api_key = key
watcher = LolWatcher(api_key)

#Cargamos el archivo .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#Definimos el Bot
bot = commands.Bot(command_prefix="!") # Prefijo de comando

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
@bot.command(name="maestry")
async def mayor_maestry(ctx,my_region,summoner_name,info):

    
  # Champs ID + Name (cambiar a base de datos .jason)
  dict_o_champs = {"266":"Aatrox","103":"Ahri","84":"Akali","12":"Alistar","32":"Amumu","34":"Anivia","1":"Annie","22":"Ashe","136":"Aurelion Sol","268":"Azir","432":"Bard","53":"Blitzcrank","63":"Brand","201":"Braum","51":"Caitlyn","164":"Camille","69":"Cassiopeia","31":"Chogath","99":"Cassiopeia","81":"Corki","122":"Darius","119":"Draven","36":"Dr. Mundo","245":"Ekko","60":"Elise","28":"Evelynn","81":"Ezreal","9":"Fiddlesticks","114":"Fiora","105":"Fizz","79":"Gangplank","104":"Graves","120":"Hecarim","74":"Heimerdinger","39":"Irelia","40":"Janna","59":"Jarvan IV","24":"Jax","126":"Jayce","222":"Jinx","429":"Kalista","43":"Karma","30":"Karthus","38":"Kassadin","55":"Katarina","10":"Kayle","141":"Kayn","85":"Kennen","121":"Kha'Zix","203":"Kindred","96":"Kog'Maw","7":"LeBlanc","64":"Lee Sin","89":"Leona","127":"Lissandra","236":"Lucian","117":"Lulu","56":"Lux","157":"Maokai","82":"Malphite","25":"Malzahar","57":"Malzahar","21":"Miss Fortune","82":"Mordekaiser","27":"Morgana","111":"Nami","33":"Nasus","91":"Nautilus","69":"Nidalee","76":"Nidalee","56":"Nocturne","20":"Nunu","4":"Olaf","61":"Orianna","80":"Pantheon","78":"Poppy","133":"Quinn","421":"Rek'Sai","58":"Renekton","107":"Rengar","92":"Riven","68":"Rumble","13":"Ryze","113":"Sejuani","35":"Shaco","98":"Shen","102":"Shyvana","27":"Singed","14":"Sion","15":"Sivir","72":"Skarner","16":"Soraka","50":"Swain","517":"Sylas","134":"Syndra","223":"Tahm Kench","163":"Taliyah","91":"Talon","44":"Taric","17":"Teemo","412":"Tresh","18":"Tristana","48":"Trundle","23":"Trymdamere","4":"Twisted Fate","29":"Twitch","77":"Udyr","6":"Urgot","110":"Varus","67":"Vayne","45":"Veigar","161":"Velkoz","711":"Vex","254":"Vi","234":"Viego","112":"Viktor","8":"Vladimir","106":"Volibear","19":"Warwick","62":"Wukong","498":"Xayah","101":"Xerath","5":"Xin Zhao","157":"Yasuo","777":"Yone","83":"Yorick","350":"Yuumi","154":"Zac","238":"Zed","221":"Zeri","268":"Ziggs","26":"Zilean","142":"Zoe","143":"Zyra"}

  # Get summoner data
  me = watcher.summoner.by_name(my_region, str(summoner_name))
  
  # Obtengo una lista con dicccionarios con la informacion de los campeones.
  total_maestry = watcher.champion_mastery.by_summoner(my_region,me['id']) # Get masteries data


  # Creo Listas que guarden lo que necesitare para crear un dataframe.
  first3_mastery_champs = []
  first3_mastery_points = []
  first3_mastery_champslvl = []


  for i in range(3): # Separo las listas dentro de total maestry para obtener toda la informacion de los campeones. # Obtengo el nombre ID de los campeones y los guardo en una lista
     first3_mastery_champs.append(total_maestry[i]['championId'])
     first3_mastery_points.append(total_maestry[i]['championPoints'])
     first3_mastery_champslvl.append(total_maestry[i]['championLevel'])

  # Obtengo los champs de la lista de IDs y los guardo en variables
  champID1 = first3_mastery_champs[0]
  champID2 = first3_mastery_champs[1]
  champID3 = first3_mastery_champs[2]

  # Obtengo el nombre de los campeones y los guardo en variables para posibles usos
  champ_name1 = dict_o_champs[f"{champID1}"]
  champ_name2 = dict_o_champs[f"{champID2}"]
  champ_name3 = dict_o_champs[f"{champID3}"]

 # Agrego estos valores a una lista para mostrarlos en pantalla.
  lista_de_champs = [champ_name1, champ_name2, champ_name3]

  if info == "Maestry":
     response = first3_mastery_points
     await ctx.send(response)
     #return first3_mastery_points
  elif info == "Level":
     response = first3_mastery_champslvl
     await ctx.send(response)
     #return first3_mastery_champslvl
  elif info == "Name":
     response = lista_de_champs
     await ctx.send(response)
     #return lista_de_champs
  elif info == "All":
     response = [first3_mastery_points, first3_mastery_champslvl, lista_de_champs]
     await ctx.send(response)
     #return total_maestry
  elif info == "Allstr":
     response = f"Tus personajes con maestria mas alta son: {champ_name1}, con {first3_mastery_points[0]} ,{champ_name2} con {first3_mastery_points[1]} y {champ_name3} con {first3_mastery_points[2]} \n y sus niveles son {first3_mastery_champslvl} respectivamente."
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
def what_is_my_team(my_region, summoner_name, match_num):

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

  #participant = participants[0]
  #participant_team = participant["teamId"]
  #print(participant_team)

  for player in participants:
     if player["teamId"] == 100:
        blue_team.append(player["summonerName"])
   
  for player in participants:
     if player["teamId"] == 200:
        red_team.append(player["summonerName"])
   

  return blue_team, red_team


bot.run(TOKEN)
# Falta crear una funcion que devuelva la duracion de la partida por ID





















