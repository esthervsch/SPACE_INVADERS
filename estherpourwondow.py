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
list_invader = [] #liste des invaders en tant qu'objet
list_invader_view = [] #liste des invaders en tant qu'objets du canvas



def pop_up_invader() :          #gère l'apparition des invaders
    
    coordX = width/2
    coordY = 100
    types = random.choice([1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3]) #genère un nombre aléatoire entre 1 et 3 avec différentes probabilités pour choisir le type d'invader :(1, 2, 3), p=[0.5, 0.35, 0.15]
    invader = Invader(coordX, coordY, types)  #centre de la fenetre en haut
    invader.imagefile = invader.imagefile[invader.type-1] #on lui assigne l'image corespondante (remplace la liste par le choix)
    invader.Hp = invader.Hp[types-1]
    list_invader.append(invader) #On ajoute l'invader à la liste d'invaders
    window.after(5000, pop_up_invader) #nouvel invader toutes les 10s
    return list_invader
pop_up_invader()#on attend pas pour faire apparaitre le premier invader

newinvader = list_invader[len(list_invader)-1]
img_invader = PhotoImage(file = newinvader.imagefile)
invader_view = canvas.create_image(newinvader.coordX, newinvader.coordY, image=img_invader)
list_invader_view.append(invader_view) #On ajoute le canvas de l'invader à la liste des canvas d'invaders


#Déplacement des invaders
def move_invaders() :
    for i, val in enumerate(list_invader):
        val.move()
        canvas.moveto(list_invader_view[i-1], val.coordX , val.coordY)
    window.after(1000, move_invaders) #répete le mouvement toutes les secondes
move_invaders()






def clavier(event) :
    key = event.keysym
    if key == 'Left' :
        player.coordX -= 5
    if key == 'Right' :
        player.coordX += 5
    canvas.coords(player_view, player.coordX , player.coordY)
window.bind('<Key>',clavier)


window.mainloop()



