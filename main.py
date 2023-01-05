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


import keyboard #mettre ds  programme principal




#Nouvelle partie
def starty(s) :
    if s==1:
        score = 0
        speed0 = 10
        level = 1



        
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

#Pour ajouter éléments à tk : créér un compte pour chaque list, if compte varie : ajouter / supr élement