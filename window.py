"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Fenetre de jeu
"""


from tkinter import Tk, Frame, Label, Button, PhotoImage, Canvas

window = Tk()
window.title("Space Invaders")

#Création canevas
height = 400
width = 300
photo_background = PhotoImage(file = "background.png")
canevas = Canvas(window, width = width, height = height, bg = 'background.png')
canevas.pack()

#Création des différentes frames
labelScore = Label(window, text = "Score = ", relief = "flat") #definir score
labelScore.pack()

Menu = Frame(window)



"""
buttonStart = Button(window, text = "Start game", command = Start) #fefinir fonction start
buttonStart.pack()
"""

buttonQuitter = Button(window, text = "Quit game", command = window.destroy)
buttonQuitter.pack()




window.mainloop()
