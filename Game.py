"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Classe Game
"""
from math import sqrt

        
class Game :
    def __init__ (self, level, score, speed) :
        self.level = level
        self.score = score
        self.speed = speed
        self.difficulty = sqrt(level)
        """
    def nextlevel ()
        self.level +=1
        self.speed = self.speed*self.difficulty
        
"""



