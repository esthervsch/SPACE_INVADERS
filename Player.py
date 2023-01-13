"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Classe Player
"""
from Game import Game
game = Game(1) #a retier

class Player :
    def __init__(self, coordX, coordY) :
        self.coordX = coordX
        self.coordY = coordY
        self.speed = 10
        self.score = 0
        self.name = "no name" #inutile?
        self.Hp = 1000
        self.freq = 10
    
    def hit(self) :
        self.Hp -= 20*game.difficulty #perte de point par miscille
        

    