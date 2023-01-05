"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Classe Missile
"""



class Missile :
    def __init__(self, coordX, coordY, points) :
        self.coordX = #retrieve from ship
        self.coordY = #retrieve from ship
        self.points = self.difficulty*10
    def move(self) :
        self.coordY += game.speed*5

