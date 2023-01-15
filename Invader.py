"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Classe Invader
"""
import random

class Invader :                #cette classe décrit 3 types d'invaders
    def __init__(self, coordX, coordY, type, game) :
        self.coordX = coordX
        self.coordY = coordY
        self.type = type
        self.view = None
        self.Hplist = [200*game.difficulty, 300*game.difficulty, 500*game.difficulty]
        self.Hp = None
        self.speed = [game.speed,game.speed]         #dépend du level
        self.imagefile = ["images/invader1.png", "images/invader2.png", "images/invader3.png"]
        self.game = game
        
    def move(self, width) :
        #On déplace en fonction du type d'invader
        #type 1 :mouvements transversaux
        #type 2 :descend et mouvements transversaux
        #type 3 : descend et mouvement transversaux randoms
        if self.coordX >= (width-40) or self.coordX <= 40 :
            self.speed[0] = -self.speed[0]
            if self.type == 1 :
                self.coordY += 40
        if self.type == 1 :
            self.coordX += self.speed[0]       #on ajout à l'ordonnée une valeur dépendant du niveau 
        if self.type == 2 :
            self.coordX += self.speed[0]
            self.coordY += self.speed[1]*0.3
        if self.type == 3 :
            self.coordX += self.speed[0]*random.choice([-1,1])
            self.coordY += self.speed[1]*0.5
    def hit(self) :
        self.Hp -= 20*self.game.difficulty #perte de point par miscille
        