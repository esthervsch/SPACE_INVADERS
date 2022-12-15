"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Fenetre de jeu
"""


from tkinter import *


window = Tk()
window.title("Space Invaders")

#Création canevas
height = 800
width = 600
photo_background = PhotoImage(file = "background.png")
canevas = Canvas(window, width = width, height = height, bg = 'black')
canevas.pack()
Score =0
#Création des différentes frames


Menu = Frame(window)



"""
buttonStart = Button(window, text = "Start game", command = Start) #fefinir fonction start
buttonStart.pack()
"""

buttonQuitter = Button(window, text = "Quit game", command = window.destroy)
buttonQuitter.pack()


#Score à récup via objet player in game
Score = 0
#Add a text in Canvas
canevas.create_text(150, 50, text="Score : "+str(Score), fill="white", font=('Helvetica 15 bold'))
canevas.pack()
#déplacement alien
img_alien = PhotoImage(file="Alien.png")
Alien = canevas.create_image(10, 10, anchor= N, image=img_alien)
x1 = 20 
y1 = 20
missile = canevas.create_rectangle(x1, y1, x1 + 10, y1 + 50,fill='red')

def move(event):
    if event.char == "q":
        canevas.move(Alien, -10, 0)
    elif event.char == "d":
        canevas.move(Alien, 10, 0)
window.bind("<Key>", move)


window.mainloop()
