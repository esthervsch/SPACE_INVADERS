from Game import *
from Player import *
from Missile import *
from Invader import *
from Block import *
from tkinter import * #morrel dit ok

window = Tk()
window.title("Space Invaders")
height = 600
width = 400
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
player_view = canvas.create_image(player.coordX, player.coordY, image=img_player)

def clavier(event) :
    key = event.keysym
    if key == 'Left' :
        player.coordX -= 5
    if key == 'Right' :
        player.coordX += 5
    canvas.coords(player_view, player.coordX , player.coordY)
window.bind('<Key>',clavier)


window.mainloop()