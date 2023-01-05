"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Classe blocks
"""



class blocks :
    def __init__(self, Hp, position, hitBox):
        self.Hp = Hp
        self.position = position
        self.hitBox = hitBox