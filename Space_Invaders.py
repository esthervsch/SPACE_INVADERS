"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Fenetre de jeu
"""
from Game import *
game = Game(1, 0, 1)
from Player import *
from Missile import *
from Invader import *
from Block import *
from tkinter import * #morrel dit ok
import random

window = Tk()
window.title("Space Invaders")

#Création des différentes frames
menu = Frame(window, relief = "groove", bg = "white")
menu.pack(side="bottom")

frame_score = Frame(window, relief = "groove", bg = "white")
frame_score.pack(side = "top")

#Création canevas
height = 500
width = 400

canvas = Canvas(window, width = width, height = height, bg="black")
canvas.pack()

#mise en place background
#photo_background = PhotoImage(file = "background.png")
#photo_backgroundbis = photo_background.zoom(x = )
#canvas.create_image(0, 0, image=photo_backgroundbis)



#Initialisation jeu
play = 0 #La partie commence pour play = 1

list_missile_player = [] #liste des missiles du joueur en tant qu'objet
list_invader = [] #liste des invaders en tant qu'objet
list_invader_img_reset = [] 
for i in range(100) :
    i = None
    list_invader_img_reset.append(i)
list_invader_img = list(list_invader_img_reset) #liste des invaders en tant qu'images
num_invader = 0
list_missile_invader = [] #liste des missiles d'invader en tant qu'objet
list_block = []
img_player = None
player = None

def reset() :
    game.nextlevel()
    canvas.delete('all')
    list_missile_player.clear()
    list_invader.clear()
    global list_invader_img
    list_invader_img = list(list_invader_img_reset)
    list_missile_invader.clear()
    list_block.clear()
    global num_invader
    num_invader = 0
    
#Nouvelle partie
def newgame() :
    if play==1:
        global player
        player = pop_up_player()
        window.bind('<Key>',clavier)
        pop_up_bloc()
        pop_up_invader()
        move_invaders()
        invader_fire()
        move_missile()
        repeat()
        
def start():
    global play
    play = 1
    newgame()

#Construction menu
buttonQuitter = Button(menu, text = "Quit game", command = window.destroy).pack(side = "left")
buttonStart = Button(menu, text = "Start game", command = start).pack(side = "right")

#Affichage score
score_view = Label(frame_score, text = "Score : " + str(game.score)) #font = ('Helvetica', 10))
score_view.pack()

def show_score() :
    global score_view
    score_view.config(text = "Score : " + str(game.score))
    

#Chargement du joueur
def pop_up_player() :
    global img_player
    img_player = PhotoImage(file="images/player.png")
    player = Player(width/2, height - img_player.height() + 30, game)
    player.view = canvas.create_image(player.coordX, player.coordY, image=img_player)
    return player

#Chargement des blocs
def pop_up_bloc() :
    block_width = width/21
    block_height = 20
    positionstartX = block_width #position de début des obstacle(=ensemble de bloc) abscisse
    positionstartY = height - img_player.height() - block_height#position de début des obstacle(=ensemble de bloc) ordonné
    while positionstartX <= 15*block_width : #On créé 3 obstacles
        nbr_block = 5 #nombre de block par ligne (pour chaque obstacle)
        block_type = 0
        while nbr_block >= 1 : #boucle qui créée un obstable
            for i in range(nbr_block) : #boucle qui créée un ligne de l'obstacle
                block = Block(game.level + block_type, game)
                block.var_color()
                block.view = canvas.create_rectangle(positionstartX, positionstartY, positionstartX + block_width, positionstartY + block_height, fill= block.color)
                list_block.append(block)
                positionstartX += block_width
            positionstartX -= (nbr_block - 1) * block_width
            positionstartY -= block_height
            nbr_block -= 2
            block_type += 1
        positionstartX += 4*block_width
        positionstartY += 3*block_height

#Variartion couleur des blocs
def bloc_color(block) :
    block.var_color()
    canvas.itemconfig(block.view, fill = block.color)

#images des invaders
def pop_up_invader() :          #gère l'apparition des invaders
    coordX = width/2
    coordY = 50
    types = random.choice([1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3]) #genère un nombre aléatoire entre 1 et 3 avec différentes probabilités pour choisir le type d'invader :(1, 2, 3), p=[0.5, 0.35, 0.15]
    invader = Invader(coordX, coordY, types, game)  #centre de la fenetre en haut
    invader.imagefile = invader.imagefile[invader.type-1] #on lui assigne l'image corespondante (remplace la liste par le choix)
    invader.Hp = invader.Hplist[types-1]
    list_invader.append(invader) #On ajoute l'invader à la liste d'invaders
    global list_invader_img
    global num_invader
    print(str(num_invader))
    list_invader_img[num_invader]= PhotoImage(file = invader.imagefile)
    invader.view = canvas.create_image(invader.coordX, invader.coordY, image=list_invader_img[num_invader])
    num_invader += 1
    if num_invader < game.max_invader :
        window.after(10000, pop_up_invader) #nouvel invader toutes les 10s

#Déplacement des invaders
def move_invaders() :
    for invader in list_invader :
        invader.move()
        canvas.coords(invader.view, invader.coordX , invader.coordY)
    window.after(200, move_invaders) #répete le mouvement toutes les 0,2 secondes

#Apparition des tirs des invaders
def invader_fire() :
    for invader in list_invader :
        missile = Missile(invader.coordX, invader.coordY, game)
        list_missile_invader.append(missile)
        missile.view = canvas.create_line(missile.coordX, missile.coordY, missile.coordX, missile.coordY + 10, fill = 'red')
    window.after(1000, invader_fire) #nouveau tir toutes les secondes

#Joueur tir
def player_fire() :
    missile = Missile(player.coordX, player.coordY, game)
    list_missile_player.append(missile)
    missile.view = canvas.create_line(missile.coordX, missile.coordY, missile.coordX, missile.coordY + 10, fill = 'blue')

    
#Déplacement des miscilles
def move_missile() :
    for missile in list_missile_invader :
        missile.move(1)
        canvas.coords(missile.view, missile.coordX, missile.coordY, missile.coordX, missile.coordY + 10)
    for missile in list_missile_player :
        missile.move(-1)
        canvas.coords(missile.view, missile.coordX, missile.coordY, missile.coordX, missile.coordY + 10)
    window.after(200, move_missile)

#Récupérer la list des éléments superposés à élément
def surface(element) :
    position = canvas.bbox(element.view) #liste avec les coordonnées (4) de la photo du joueur 
    if not(isinstance(position, tuple)) :
        print('vide')
    list_touch = canvas.find_overlapping(position[0], position[1], position[2], position[3]) #liste des élément touchant/étant superposés au player
    return list_touch

#Perte de points de vie joueur
def player_touched() :
    list_touch_player = surface(player)
    for item in list_touch_player :
        for missile in list_missile_invader : 
            if item == missile.view : #si l'élément est un missile
                player.hit()
                list_missile_invader.remove(missile)
                canvas.delete(missile.view)
        for invader in list_invader :
            if item == invader.view : #si l'élément est un invader
                player.Hp = 0
                gameover()
                
    window.after(50, player_touched)

#Perte de points de vie invader
def invader_touched() :
    for invader in list_invader :
        list_touch_invader = surface(invader)
        for item in list_touch_invader :
            for missile in list_missile_player : 
                if item == missile.view : #si l'élément est un missile
                    invader.hit()
                    list_missile_player.remove(missile)
                    canvas.delete(missile.view)
    window.after(50, invader_touched)

#Perte de points de vie block
def block_touched() :
    for block in list_block :
        list_touch_block = surface(block)
        for item in list_touch_block :
            for missile in list_missile_invader :
                if item == missile.view :
                    block.hit()
                    bloc_color(block)
                    list_missile_invader.remove(missile)
                    canvas.delete(missile.view)
            for missile in list_missile_player :
                if item == missile.view :
                    list_missile_player.remove(missile)
                    canvas.delete(missile.view)
            for invader in list_invader :
                if item == invader :
                    list_invader.remove(invader)
                    canvas.delete(invader.view)
                    
                        

#Perte de vie (player, invader ou bloc)
def killed(list) :
    #A faire tourner régulièrement
    #objet peut être un invader, un bloc ou un missile
    #list est la liste correspondante contenant l'objet
    #supprime un élément n'ayant plus de point de vie
    for objet in list :
        if objet.Hp <= 0 :
            if list == list_invader :
                game.score += objet.Hplist[objet.type-1] #le score augmente du nombre de pv le l'ennemi tué
            list.remove(objet)
            canvas.delete(objet.view)
            

def out_canvas(list_missile) : #On supprime les éléments en dehors du canvas
    for missile in list_missile :
        if missile.coordY >= height or missile.coordY <= 0 :
            list_missile.remove(missile)
            canvas.delete(missile.view)

def gameover() :
    if player.Hp <= 0 :
        canvas.delete('all')

def level_won() :
    reste_invader = 0
    for invader in list_invader :
        reste_invader += invader.Hp
    if reste_invader == 0 and num_invader == game.max_invader: #si les invaders sont tous mort
        reset()
        newgame()

def repeat() :
    #On appelle ici les fonction devant tourner constamment
    block_touched()
    invader_touched()
    player_touched()
    killed(list_block)
    killed(list_invader)
    gameover()
    level_won()
    out_canvas(list_missile_invader)
    out_canvas(list_missile_player)
    show_score()
    window.after(50,repeat)

def clavier(event) :
    key = event.keysym
    if key == 'Left' :
        player.coordX -= player.speed
    if key == 'Right' :
        player.coordX += player.speed
    canvas.coords(player.view, player.coordX , player.coordY)
    if key == 'space' :
        player_fire()

window.mainloop()