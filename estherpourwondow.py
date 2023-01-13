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
list_invader_img = [] #liste des invaders en tant qu'images
for i in range(100) :
    globals()['img_invader' + str(i-1)] = None
    list_invader_img.append('img_invader' + str(i-1))

compte = 0
def pop_up_invader() :          #gère l'apparition des invaders
    coordX = width/2
    coordY = 100
    types = random.choice([1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3]) #genère un nombre aléatoire entre 1 et 3 avec différentes probabilités pour choisir le type d'invader :(1, 2, 3), p=[0.5, 0.35, 0.15]
    global compte
    name = 'invader' + str(compte) 
    print(name)
    invader = Invader(coordX, coordY, types, name)  #centre de la fenetre en haut
    invader.imagefile = invader.imagefile[invader.type-1] #on lui assigne l'image corespondante (remplace la liste par le choix)
    invader.Hp = invader.Hp[types-1]
    list_invader.append(invader) #On ajoute l'invader à la liste d'invaders
    global list_invader_img
    list_invader_img[compte]= PhotoImage(file = invader.imagefile)
    invader.name = canvas.create_image(invader.coordX, invader.coordY, image=list_invader_img[compte])
    compte += 1
    window.after(5000, pop_up_invader) #nouvel invader toutes les 10s
    return list_invader
pop_up_invader() #on attend pas pour faire apparaitre le premier invader



#Déplacement des invaders
def move_invaders() :
    for val in list_invader :
        val.move()
        canvas. coords(val.name, val.coordX , val.coordY)
        val.Hp -= 1
    window.after(200, move_invaders) #répete le mouvement toutes les secondes
move_invaders()

#Apparition des tirs
list_missiles = [] #liste des invaders en tant qu'objet
list_missiles_img = [] #liste des invaders en tant qu'images
for i in range(500) :
    globals()['img_missile' + str(i-1)] = None
    list_missiles_img.append('img_missile' + str(i-1))
    
def pop_up_missile() :
    for val in list_invader


#Perte de vie (player, invader ou bloc)
def die() :
    if player.Hp <= 0 :
        #game over
        a=1 #A retirer
    for val in list_invader :
        if val.Hp <= 0 :
            list_invader.remove(val)
            canvas.delete(val.name)
    window.after(10,die)
die()

def clavier(event) :
    key = event.keysym
    if key == 'Left' :
        player.coordX -= 5
    if key == 'Right' :
        player.coordX += 5
    canvas.coords(player_view, player.coordX , player.coordY)
window.bind('<Key>',clavier)

        
window.mainloop()