from funciones import *

class Match():
    def __init__(self,num_partida,servidor,invocador):

        self.id = list_of_matchs(servidor,invocador,num_partida)
        self.tipo = None#tipo
        self.servidor = servidor
        self.duration = None#duration
        self.team_red = None#team_red
        self.team_blue = None#team_blue
        self.team_red_result = None#team_red_result 
        self.team_blue_result = None#team_blue_result
