"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Fenetre de jeu
"""


from tkinter import Tk, Label, Button, PhotoImage

window = Tk()
window.title("Space Invaders")

labelScore = Label(window, text = "Score = ")
labelScore.pack()

buttonQuitter = Button(window, text = "Quit game", command = window.destroy)
buttonQuitter.pack()

window.mainloop()
