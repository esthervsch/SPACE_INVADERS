from Game import *
from Player import *
from Missile import *
from Invader import *
from Block import *
from tkinter import * #morrel dit ok
import random
from time import sleep

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



#Cargement des images
#image du joueur
player = Player(width/2, height-78)  #78 = hauteur image +10
img_player = PhotoImage(file="images/player.png")
player_view = canvas.create_image(player.coordX, player.coordY, image=img_player)

#images des invaders
list_invader=[]




def pop_up_invader() :          #gère l'apparition des invaders
    coordX = width/2
    coordY = 0
    invader = Invader(coordX, coordY)  #centre de la fenetre en haut
    type = random.choice((1, 2, 3), p=[0.5, 0.35, 0.15]) #genère un nombre aléatoire entre 1 et 3 avec différentes probabilités pour choisir le type d'invader
    img_invader_file = invader.images[type-1] #on lui assigne l'image corespondante
    img_invader = PhotoImage(file = img_invader_file)
    Hp = invader.Hpmax[type-1]
    invadercarac = [type, coordX, coordY, Hp]     #on créée une liste ragrouppant les caractéristiques de l'invader aléaoir créé
    list_invader.append(invadercarac)           #On ajoute l"invader à la liste d'invader
    invader_view = canvas.create_image(invader.coordX, invader.coordY, image=img_invader)#invader apparait
    sleep(10)       #nouvel invader toutes les 10s
pop_up_invader()

def clavier(event) :
    key = event.keysym
    if key == 'Left' :
        player.coordX -= 5
    if key == 'Right' :
        player.coordX += 5
    canvas.coords(player_view, player.coordX , player.coordY)
window.bind('<Key>',clavier)


window.mainloop()