"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Classe MissSile
"""



class Missile :
    def __init__(self, coordX, coordY, points) :
        self.coordX = 0#retrieve from ship
        self.coordY = 0#retrieve from ship
        self.points = self.difficulty*10
    def move(self) :
        self.coordY += Game.speed*5

