"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Classe Invader
"""
from Game import Game
import random
game = Game(1) #a retier
class Invader :                #cette classe décrit 3 types d'invaders
    def __init__(self, coordX, coordY, type, name) :
        self.coordX = coordX
        self.coordY = coordY
        self.type = type
        self.name = name
        self.Hp = [100*game.difficulty, 150*game.difficulty, 250*game.difficulty]
        self.speed = [game.speed,game.speed]         #dépend du level
        self.freq = 3
        self.imagefile = ["images/invader1.png", "images/invader2.png", "images/invader3.png"]
        
 
    def move(self) :
        #On déplace en fonction du type d'invader
        #type 1 :mouvements transversaux
        #type 2 :descend et mouvements transversaux
        #type 3 : descend et mouvement transversaux randoms
        if self.coordX>= 360 or self.coordX<=40 :
            self.speed[0] = -self.speed[0]
            if self.type == 1 :
                self.coordY += 40
        if self.type == 1 :
            self.coordX += self.speed[0]*5       #on ajout à l'ordonnée une valeur dépendant du niveau 
        if self.type == 2 :
            self.coordX += self.speed[0]*5
            self.coordY += self.speed[1]
        if self.type == 3 :
            self.coordX += self.speed[0]*5*random.choice([-1,1])
            self.coordY += self.speed[1]*2
    #def fire(self) :
        