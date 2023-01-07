from Game import *
from Player import Player
from Missile import *
from Invader import *
from Block import *
from tkinter import * #morrel dit ok
import keyboard 
window = Tk()
window.title("Space Invaders")
height = 800
width = 600
canvas = Canvas(window, width = width, height = height, bg="black")
canvas.pack()




#Nouvelle partie
def starty(s) :
    if s==1:
        score = 0
        speed0 = 10
        level = 1

player = Player(width/2, height-78)  #78 = hauteur image +10

img_player = PhotoImage(file="player.png")
player_view = canvas.create_image(player.coordX ,player.coordY , anchor= N, image=img_player)

keyboard.on_press_key('left', lambda _:canvas.move(player_view, -10, 0)) #mettre speed au lieu de 10/-10
keyboard.on_press_key("right", lambda _:canvas.move(player_view, 10, 0))











window.mainloop()