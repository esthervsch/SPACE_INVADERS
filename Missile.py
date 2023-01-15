"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Classe MissSile
"""
import random

class Missile :
    def __init__(self, coordX, coordY, game) :
        self.coordX = coordX
        self.coordY = coordY
        self.view = None
        self.Hp = 20 #nbr de points retirer quand il touche une cible
        self.game = game

    def move(self, sens) :
        self.coordY += self.game.speed*sens*15

