"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Classe Player
"""

class Player :
    def __init__(self, coordX, coordY, game) :
        self.coordX = coordX
        self.coordY = coordY
        self.Hp = 500
        self.speed = 5
        self.view = None
        self.game = game

    def hit(self) :
        self.Hp -= 20*self.game.difficulty #perte de point par miscille
    
    def move(self, sens, width) : #sens négatif si vers la gauche
        self.coordX += self.speed*sens
        if self.coordX >= width :
            self.coordX -= width
        if self.coordX <= 0 :
            self.coordX += width
        

    