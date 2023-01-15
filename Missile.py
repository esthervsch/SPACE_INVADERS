"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Classe MissSile
"""


class Missile :
    def __init__(self, coordX, coordY, game) :
        self.coordX = coordX
        self.coordY = coordY
        self.view = None
        self.game = game

    def move(self, sens) :
        self.coordY += self.game.speed*sens*3

