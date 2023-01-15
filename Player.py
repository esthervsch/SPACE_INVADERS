"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Classe Player
"""
import random
#from Game import Game
#game = Game(1,0,1)

class Player :
    def __init__(self, coordX, coordY, game) :
        self.coordX = coordX
        self.coordY = coordY
        self.Hp = 1000
        self.speed = 10
        self.freq = 10
        self.view = None
        self.game = game
    def hit(self) :
        self.Hp -= 20*self.game.difficulty #perte de point par miscille
        print(str(self.Hp))
        

    