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



#Cargement des images
#image du joueur
player = Player(width/2, height-78)  #78 = hauteur image +10
img_player = PhotoImage(file="invader1.png")
player_view = canvas.create_image(player.coordX, player.coordY, image=img_player)

#images des invaders
invader = Invader(width/2, height-78)  #78 = hauteur image +10
img_player = PhotoImage(file="invader1.png")
player_view = canvas.create_image(player.coordX, player.coordY, image=img_player)

def pop_up_invader(invader) :          #gère l'apparition des invaders
        type = random.choice((1, 2, 3), p=[0.5, 0.35, 0.15]) #genère un nombre aléatoire entre 1 et 3 avec différentes probabilités pour choisir le type d'invader
        coordX = width/2 # on met en abscisse le centre de la fenetre
        coordY = 0
        Hp = invader.Hpmax[type-1]
        invadercarac = [type, coordX, coordY, Hp]     #on créée une liste ragrouppant les caractéristiques de l'invader aléaoir créé
        invader.list.append(invadercarac)           #On ajoute l"invader à la liste d'invader
        #invader apparait
        sleep(10)       #nouvel invader toutes les 10s


def clavier(event) :
    key = event.keysym
    if key == 'Left' :
        player.coordX -= 5
    if key == 'Right' :
        player.coordX += 5
    canvas.coords(player_view, player.coordX , player.coordY)
window.bind('<Key>',clavier)


window.mainloop()