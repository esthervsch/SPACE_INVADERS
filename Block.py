"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Classe Block
"""
import random

class Block() :
    def __init__(self, type, game):
        self.type = type
        self.Hp = 50*self.type
        self.color = None
        self.colorlist = ['deeppink', 'mediumpurple', 'deepskyblue', 'limegreen', 'yellow', 'darkorange', 'red']
        self.view = None
        self.game = game

    def hit(self) :
        self.Hp -= 20*self.game.difficulty

    def var_color(self) : #Couleur des block dépendant de leur point de vie
        choixcouleur = int((self.Hp-1)/50)
        if choixcouleur > len(self.colorlist) :
            choixcouleur -= len(self.colorlist)
        self.color = self.colorlist[choixcouleur]










