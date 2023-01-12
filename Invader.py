"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Classe Invader
"""
from Game import Game
game = Game(1) #a retier
class Invader :                #cette classe décrit 3 types d'invaders
    def __init__(self, coordX, coordY, type, name) :
        self.coordX = coordX
        self.coordY = coordY
        self.type = type
        self.name = name
        self.Hp = [100*game.difficulty, 150*game.difficulty, 250*game.difficulty]
        self.speed = game.speed         #dépend du level
        self.freq = 3
        self.imagefile = ["images/invader1.png", "images/invader2.png", "images/invader3.png"]
        


    def move(self) :
        #On déplace en fonction du type d'invader
        #type 1 :descend
        #type 2 :mouvements tranversaux
        #type 3 : descend et mouvements transversaux
        if self.type == 1 :
            self.coordY += self.speed*5       #on ajout à l'ordonnée une valeur dépendant du niveau 
        if self.type == 2 :
            self.coordX += self.speed*5
        if self.type == 3 :
            self.coordX += self.speed*5
            self.coordY += self.speed*5

    #def fire(self) :
        

    def killed(self) :
        for i in len(self.list) :
            if self.list[i][3] == "0" :
                self.list[i]





