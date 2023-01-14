"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Classe Block
"""


class Block() :
    def __init__(self, type):
        self.type = type
        self.Hp = 50*self.type
        self.color = ['mediumpurple', 'deepskyblue', 'limegreen', 'yellow', 'darkorange', 'red']
        self.view = None














