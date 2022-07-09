
from funciones import list_of_matchs,gamemode,gameDuration,what_is_my_team,whowin_in

class Match():
    def __init__(self,match_num,my_region,summoner_name,):

        self.id =  list_of_matchs(my_region,summoner_name,match_num)
        self.tipo = gamemode(my_region,summoner_name,match_num)
        self.servidor = my_region
        self.duration = gameDuration(my_region, summoner_name, match_num) / 60
        self.team_red = what_is_my_team(my_region, summoner_name, match_num)[1]
        self.team_blue = what_is_my_team(my_region, summoner_name, match_num)[0]
        self.team_red_result = whowin_in(my_region,summoner_name,match_num,"red")
        self.team_blue_result = whowin_in(my_region,summoner_name,match_num,"blue")



match1 = Match(0,"la2","XxSoul MasterxX")
print(match1.team_blue)
print(match1.team_red)
print(match1.team_blue_result)
print(match1.team_red_result)
print(match1.duration)
print(match1.tipo)
print(match1.id)
