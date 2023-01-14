"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Classe Block
"""
from Game import Game
game = Game(1) #a retier

class Block() :
    def __init__(self, type):
        self.type = type
        self.Hp = 50*self.type
        self.color = None
        self.colorlist = ['deeppink', 'mediumpurple', 'deepskyblue', 'limegreen', 'yellow', 'darkorange', 'red']
        self.view = None

    def hit(self) :
        self.Hp -= 20*game.difficulty
        
    
    def var_color(self) : #Couleur des block dépendant de leur point de vie
        choixcouleur = int((self.Hp-1)/50)
        if choixcouleur > len(self.colorlist) :
            choixcouleur -= len(self.colorlist)
        self.color = self.colorlist[choixcouleur]










