"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Classe Player
"""


class Player :
    def __init__(self, coordX, coordY, speed, freq, Hp, score, name) :
        self.coordX = #mileu pour le début
        self.coordY = #bas de jeu, invariable
        self.speed = 10
        self.score = 0
        self.name = "no name" #inutile?
        self.Hp = 1000
    def move(self) :
