from Game import *
from Player import *
from Missile import *
from Invader import *
from Block import *
from tkinter import * #morrel dit ok
window = Tk()
window.title("Space Invaders")
canvas = Canvas(window, width = 100, height = 100, bg="black")
canvas.pack()




#Nouvelle partie
def starty(s) :
    if s==1:
        score = 0
        speed0 = 10
        level = 1



img_player = PhotoImage(file="")
player = canvas.create_image(Player.coordX ,Player.coordY , anchor= N, image=img_player)









