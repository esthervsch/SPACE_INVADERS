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
        self.view = None
        self.Hp = 20 #nbr de points retirer quand il touche une cible

    def move(self, sens) :
        self.coordY += game.speed*sens*15

