import Game
import Player
import Missile 
import Invader
import Block
from tkinter import * #morrel dit ok

window = Tk()
window.title("Space Invaders")
height = 800
width = 600
canvas = Canvas(window, width = width, height = height, bg="black")
canvas.pack()




#Nouvelle partie
def starty(s) :
    if s==1:
        score = 0
        speed0 = 10
        level = 1

player = Player(width/2, height-78)  #78 = hauteur image +10

img_player = PhotoImage(file="player.png")
player_view = canvas.create_image(player.coordX ,player.coordY , anchor= N, image=img_player)


def keyboard(event) :
    global playercoordX,playercoordY
    key = event.keysym
    if key == 'left' :
        playercoordX -= 10
    if key == 'right' :
        playercoordX += 10
    canvas.coords(player_view, player.coordX + playercoordX, player.coordY)






window.mainloop()