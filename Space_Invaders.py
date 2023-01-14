"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Fenetre de jeu
"""
from Game import *
from Player import *
from Missile import *
from Invader import *
from Block import *
from tkinter import * #morrel dit ok
import random

window = Tk()
window.title("Space Invaders")

#Création canevas
height = 600
width = 400

canvas = Canvas(window, width = width, height = height, bg="black")
canvas.pack()

#mise en place background
#photo_background = PhotoImage(file = "background.png")
#photo_backgroundbis = photo_background.zoom(x = )
#canvas.create_image(0, 0, image=photo_backgroundbis)


#Création des différentes frames
ranking = Frame(window, relief="groove")
ranking.pack(side="left")
menu = Frame(window, relief="groove", bg="white")
menu.pack(side="bottom")

#Nouvelle partie
def starty(s) :
    if s==1:
        score = 0
        speed0 = 10
        level = 1

s=0
def schange():
    s=1
    starty(s)


buttonQuitter = Button(menu, text = "Quit game", command = window.destroy).pack()
buttonStart = Button(window, text = "Start game", command = schange).pack()


#Score à récup via objet player in game
score= game.score
#Add a text in Canvas
canvas.create_text(150, 50, text="Score : "+str(score), fill="white", font=('Helvetica 15 bold'))
canvas.pack()


list_missile_player = [] #liste des missiles du joueur en tant qu'objet
list_invader = [] #liste des invaders en tant qu'objet
list_invader_img = [] #liste des invaders en tant qu'images
for i in range(100) :
    globals()['img_invader' + str(i-1)] = None
    list_invader_img.append('img_invader' + str(i-1))
num_invader = 0
list_missile_invader = [] #liste des missiles d'invader en tant qu'objet
list_bloc = []

#Chargement du joueur
img_player = PhotoImage(file="images/player.png")
player = Player(width/2, height - img_player.height() + 30)
player.view = canvas.create_image(player.coordX, player.coordY, image=img_player)

#Chargement des blocs
#34 blocs 21 / 30
block_width = width/21
block_height = 20
positionstartX = block_width #position de début des obstacle(=ensemble de bloc) abscisse
positionstartY = height - img_player.height() - block_height#position de début des obstacle(=ensemble de bloc) ordonné
while positionstartX <= 15*block_width : #On créé 3 obstacles
    nbr_block = 5 #nombre de block par ligne (pour chaque obstacle)
    while nbr_block >= 1 :
        for i in range(nbr_block) : #on créé 34 blocs
            block = Block(1)
            block.color = block.color[block.type]
            block.view = canvas.create_rectangle(positionstartX, positionstartY, positionstartX + block_width, positionstartY + block_height, fill= block.color[block.type-1])
            positionstartX += block_width
        positionstartX -= (nbr_block -1) * block_width
        nbr_block -= 2
        positionstartY -= block_height
    positionstartX += 4*block_width
    positionstartY += 3*block_height

#images des invaders
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
def invader_fire() :
    for invader in list_invader :
        missile = Missile(invader.coordX, invader.coordY)
        list_missile_invader.append(missile)
        missile.view = canvas.create_line(missile.coordX, missile.coordY, missile.coordX, missile.coordY + 10, fill = 'red')
    window.after(1000, invader_fire) #nouveau tir toutes les secondes
    return list_missile_invader
invader_fire()

#Joueur tir
def player_fire() :
    missile = Missile(player.coordX, player.coordY)
    list_missile_player.append(missile)
    missile.view = canvas.create_line(missile.coordX, missile.coordY, missile.coordX, missile.coordY + 10, fill = 'blue')
    #return list?
    
#Déplacement des miscilles
def move_missile() :
    for missile in list_missile_invader :
        missile.move(1)
        canvas.coords(missile.view, missile.coordX, missile.coordY, missile.coordX, missile.coordY + 10)
    for missile in list_missile_player :
        missile.move(-1)
        canvas.coords(missile.view, missile.coordX, missile.coordY, missile.coordX, missile.coordY + 10)
    window.after(200, move_missile)
move_missile()


#Perte de points de vie joueur
def player_touched() :
    position = canvas.bbox(player.view) #liste avec les coordonnées (4) de la photo du joueur 
    list_touch_player = canvas.find_overlapping(position[0], position[1], position[2], position[3]) #liste des élément touchant/étant superposés au player
    for item in list_touch_player :
        for missile in list_missile_invader : 
            if item == missile.view : #si l'élément est un missile
                player.hit()
                list_missile_invader.remove(missile)
                canvas.delete(missile.view)
        for invader in list_invader :
            if item == invader.view :
                player.Hp = 0
                invader.Hp = 0
    window.after(50, player_touched)
window.after(1000, player_touched)

#Perte de points de vie invader
def invader_touched() :
    for invader in list_invader :
        position = canvas.bbox(invader.view) #liste avec les coordonnées (4) de la photo de l'invader
        list_touch_invader = canvas.find_overlapping(position[0], position[1], position[2], position[3]) #liste des élément touchant/étant superposés au player
        for item in list_touch_invader :
            for missile in list_missile_player : 
                if item == missile.view : #si l'élément est un missile
                    invader.hit()
                    list_missile_player.remove(missile)
                    canvas.delete(missile.view)
    window.after(50, invader_touched)
window.after(1000, invader_touched)

#Perte de vie (player, invader ou bloc)
def killed(list) :
    #A faire tourner régulièrement
    #objet peut être un invader, un bloc ou un missile
    #list est la liste correspondante contenant l'objet
    #supprime un élément n'ayant plus de point de vie
    for objet in list :
        if objet.Hp <= 0 :
            list.remove(objet)
            canvas.delete(objet.view)
        
def gameover() :
    if player.Hp <= 0 :
        canvas.delete('all')
        
def repeat() :
    #On appelle ici les fonction devant tourner constamment
    #killed()
    gameover()
    window.after(10,repeat)
repeat()

def clavier(event) :
    key = event.keysym
    if key == 'Left' :
        player.coordX -= 5
    if key == 'Right' :
        player.coordX += 5
    canvas.coords(player.view, player.coordX , player.coordY)
    if key == 'space' :
        player_fire()
window.bind('<Key>',clavier)


window.mainloop()