"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Classe player
"""


class player :
    def __init__(self,position hitBox, Hp, score, name, life, ):
        self.hitBox = [1,1]
        self.Life = 3
        self.Score = "0"
        self.Name = "no name"
        self.Hp = 1
        self.Position = [0,1]
    def move(self) :