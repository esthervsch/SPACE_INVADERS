"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Programme principal
"""
from time import sleep
from math import sqrt
from numpy import random
from tkinter import *

#Nouvelle partie
score = 0
speed0 = 10
level = 1

#on definit les classes pour les 4 objet et le jeu

class invaders :
    def __init__(self,list, Hpmax, coordX, coordY, speed, freq, hitBox) :
        self.list = []
        self.Hpmax = [100*game.difficulty, 150*game.difficulty, 250*game.difficulty]
        self.speed = game.speed #dépend du level
        self.freq = 3

    def pop_up(self) :
        type = random.choice((1, 2, 3), p=[0.5, 0.35, 0.15]) #genère un nombre aléatoire entre 1 et 3 avec différentes probabilités pour choisir le type d'invader
        coordX = 200 # on met en abscisse le centre de la fenetre
        coordY = 0
        Hp = self.Hpmax[type-1]
        invader= [type, coordX, coordY, Hp]
        self.list.append(invader)
        #invader apparait
        sleep(10)

    def move(self) :
        for i in len(self.list) :   #On déplace en fonction du type d'invader
            if self.list[i] == 1 :
                self.list[i][2] += self.speed
            if self.list[i] == 2 :
                self.list[i][1] += self.speed
            if self.list[i] == 3 :
                self.list[i][1] += self.speed
                self.list[i][2] += self.speed
        sleep(1)
        invaders.move(self)

    def fire(self) :
        canevas.create_line(x, y, x+vitesse,)

    def killed(self) :
        for i in len(self.list) :
            if self.list[i][3] == 0
                self.list[i]

class blocks :
    def __init__(self, Hp, position, hitBox):
        self.Hp = Hp
        self.position = position
        self.hitBox = hitBox
class player :
    def __init__(self, hitbox, Hp, score, name, life, position):
        self.Hitbox = [1,1]
        self.Life = 3
        self.Score = "0"
        self.Name = "no name"
        self.Hp = 1
        self.Position = [0,1]

class missiles :
    def __init__(self, position, hitbox ):
        self.Hitbox = [1,1]
        self.Position = [0,0]
        
class game :
    def __init__ (self, world,  level, difficulty, speed):
        self.world = world
        self.level = level 
        self.difficulty = sqrt(level)
        self.speed = speed0*self.difficulty
        """
    def nextlevel
        if level passed :
            level +=1



#Score

def score() :
    score = 


"""