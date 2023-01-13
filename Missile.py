"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Classe MissSile
"""
from Game import Game
game = Game(1) #a retier

class Missile :
    def __init__(self, coordX, coordY) :
        self.coordX = coordX
        self.coordY = coordY
        self.coordYend = coordY + 10
        self.view = None
        self.points = game.difficulty*10

    def move(self, sens) :
        self.coordY += game.speed*sens*15
        self.coordYend += game.speed*sens*15

