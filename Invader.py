"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Classe Invader
"""
import Game
from time import sleep

class Invader :                #cette classe décrit 3 types d'invaders
    def __init__(self, coordX, images, coordY, Hpmax, speed, freq) :
        self.Hpmax = [100*Game.difficulty, 150*Game.difficulty, 250*Game.difficulty]
        self.speed = Game.speed         #dépend du level
        self.freq = 3
        self.images = ["images/invader1.png", "images/invader2.png", "images/invader3.png"]
        


    def move(self) :
        #On déplace en fonction du type d'invader
        #type 1 :descend
        #type 2 :mouvements tranversaux
        #type 3 : descend et mouvements transversaux
        for i in len(self.list) :
            if self.list[i][0] == 1 :
                self.list[i][2] += self.speed       #on ajout à l'ordonnée une valeur dépendant du niveau 
            if self.list[i][0] == 2 :
                self.list[i][1] += self.speed
            if self.list[i][0] == 3 :
                self.list[i][1] += self.speed
                self.list[i][2] += self.speed
        sleep(1)        #répete le mouvement toutes les secondes
        Invader.move(self)

    #def fire(self) :
        

    def killed(self) :
        for i in len(self.list) :
            if self.list[i][3] == "0" :
                self.list[i]





