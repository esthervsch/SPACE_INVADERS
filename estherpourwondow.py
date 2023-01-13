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

num_invader = 0
def pop_up_invader() :          #gère l'apparition des invaders
    coordX = width/2
    coordY = 100
    types = random.choice([1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3]) #genère un nombre aléatoire entre 1 et 3 avec différentes probabilités pour choisir le type d'invader :(1, 2, 3), p=[0.5, 0.35, 0.15]
    invader = Invader(coordX, coordY, types)  #centre de la fenetre en haut
    invader.imagefile = invader.imagefile[invader.type-1] #on lui assigne l'image corespondante (remplace la liste par le choix)
    invader.Hp = invader.Hp[types-1]
    list_invader.append(invader) #On ajoute l'invader à la liste d'invaders
    global list_invader_img
    global num_invader
    list_invader_img[num_invader]= PhotoImage(file = invader.imagefile)
    invader.view = canvas.create_image(invader.coordX, invader.coordY, image=list_invader_img[num_invader])
    num_invader += 1
    window.after(10000, pop_up_invader) #nouvel invader toutes les 10s
    return list_invader
pop_up_invader() #on attend pas pour faire apparaitre le premier invader



#Déplacement des invaders
def move_invaders() :
    for invader in list_invader :
        invader.move()
        canvas. coords(invader.view, invader.coordX , invader.coordY)
    window.after(200, move_invaders) #répete le mouvement toutes les secondes
move_invaders()

#Apparition des tirs des invaders
list_missiles_invader = [] #liste des missiles d'invader en tant qu'objet


def invader_fire() :
    for invader in list_invader :
        missile = Missile(invader.coordX, invader.coordY)
        list_missiles_invader.append(missile)
        missile.view = canvas.create_line(missile.coordX, missile.coordY, missile.coordX, missile.coordYend, fill = 'red')
    window.after(1000, invader_fire) #nouveau tir toutes les secondes
    return list_missiles_invader
invader_fire()

#Joueur tir
list_missiles_player = [] #liste des missiles du joueur en tant qu'objet

def player_fire() :
    missile = Missile(player.coordX, player.coordY)
    list_missiles_player.append(missile)
    missile.view = canvas.create_line(missile.coordX, missile.coordY, missile.coordX, missile.coordYend, fill = 'blue')

#Déplacement des miscilles
def move_missile() :
    for missile in list_missiles_invader :
        missile.move(1)
        canvas.coords(missile.view, missile.coordX, missile.coordY, missile.coordX, missile.coordYend)
    for missile in list_missiles_player :
        missile.move(-1)
        canvas.coords(missile.view, missile.coordX, missile.coordY, missile.coordX, missile.coordYend)
    window.after(500, move_missile)
move_missile()


#Perte de points de vie
def touched() :
    position = canvas.bbox(player_view) #liste avec les coordonnées (4) de la photo du joueur 
    list_touch_player = canvas.find_overlapping(position[0], position[1], position[2], position[3]) #liste des élément touchant/étant superposés au player
    for item in list_touch_player :
        for missile in list_missiles_invader : 
            if item == missile.view : #si l'élément est un missile
                player.hit()
                list_missiles_invader.remove(missile)
                canvas.delete(missile.view)
        for invader in list_invader :
            if item == invader.view :
                player.Hp = 0
                invader.Hp = 0
    window.after(50, touched)
window.after(1000, touched)

#Perte de vie (player, invader ou bloc)
def die() :
    if player.Hp <= 0 :
        #game over
        a=1 #A retirer
    for invader in list_invader :
        if invader.Hp <= 0 :
            list_invader.remove(invader)
            canvas.delete(invader.view)
    window.after(10,die)
die()

def clavier(event) :
    key = event.keysym
    if key == 'Left' :
        player.coordX -= 5
    if key == 'Right' :
        player.coordX += 5
    canvas.coords(player_view, player.coordX , player.coordY)
    if key == 'space' :
        player_fire()
window.bind('<Key>',clavier)

window.mainloop()