"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Programme principal
"""

#on definit les classes pour les 4 objet et le jeu

class invaders:
    def __init__(self, Hp, speed, hitBox):
        self.Hp  = Hp
        self.speed = speed
    def 

class blocks:
    def __init__(self, Hp, position, hitBox):
        self.Hp = Hp
        self.position = position
        self.hitBox = hitBox
class players :
    def __init__(self, Hitbox, Hp, Score, Name, Life, Position):
        self.Hitbox = [1,1]
        self.Life = 3
        self.Score = "0"
        self.Name = "no name"
        self.Hp = 1
        self.Position = [0,1]

class missiles :
    def __init__(self, Position, Hitbox ):
        self.Hitbox = [1,1]
        self.Position = [0,0]
        
class Game :
    def __init__ (self, world, players, missiles, blocks, invaders):
        

