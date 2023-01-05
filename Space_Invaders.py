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
#from Invader import *
from Block import *
from tkinter import * #morrel dit ok

window = Tk()
window.title("Space Invaders")

#Création canevas
height = 800 
width = 600

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


s=0
def schange():
    s=1
    starty(s)
    

buttonQuitter = Button(menu, text = "Quit game", command = window.destroy).pack()
buttonStart = Button(window, text = "Start game", command = schange).pack()



#Score à récup via objet player in game
score="a recup"
#Add a text in Canvas
canvas.create_text(150, 50, text="Score : "+str(score), fill="white", font=('Helvetica 15 bold'))
canvas.pack()

#déplacement alien

img_alien = PhotoImage(file="background.png")
Alien = canvas.create_image(10, 10, anchor= N, image=img_alien)
x1 = 20 
y1 = 20
missile = canvas.create_rectangle(x1, y1, x1 + 10, y1 + 50,fill='red')

def move(event):
    if event.char == "q":
        canvas.move(Alien, -10, 0)
    elif event.char == "d":
        canvas.move(Alien, 10, 0)
window.bind("<Key>", move)


window.mainloop()
