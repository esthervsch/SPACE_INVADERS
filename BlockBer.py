"""
Esther Veschambre et Bertrand Gaillet
15/12/2022
CSDEV TP4
Space_Invaders
Classe Block
"""


from tkinter import PhotoImage
class Block :
    
        
    def __init__(self, pPosition, pNumero, pWindow, pCanevas):
        """
        Méthode de création des blocs.

        Parameters
        ----------
        pPosition: Liste
            Liste de 2 entier. Coordonnée du bloc.
        pNumero : int
            Numéro de bloc. Permet de choisir quel texture afficher.
        pWindow : tkinter window
            On indique la fenêtre d'affichage
        pCanevas : tkinter canevas
            On precise le Canevas pour dessiner dessus

        Returns
        -------
        None.

        """

        self.Position = pPosition
        self.color0 = 'blue' #Permet d'afficher chacune des 5 couleurs correspondant aux dégats subbits
        self.color1 = 'green'
        self.color2 = 'yellow'
        self.color3 = 'orange'
        self.color4 = 'red'
        self.DegatSubit = 0

        # si tu veux les dessiner mais galère de faire des trou, peut être faire des carrés plus petit ?
        # create_rectangle(0, 0, 100, 100, fill="blue", outline = 'blue')
        self.imageOnCanvas = pCanevas.create_rectangle(0, 0, 100, 100, fill=self.color0, outline = 'black')

    def AffichageBloc(self, pWindow, pCanevas):
        """
        Méthode pour afficher les blocs avec l'image correspondant aux dégats qu'ils ont subit

        Parameters
        ----------
        pWindow : tkinter window
            Nécessaire pour l'interface graphique.
        pCanevas : tkinter canevas
            Idem.

        Returns
        -------
        None.

        """
        if self.DegatSubit == 0:    #Si le bloc a subit 0 dégat, etc...
            self.Image = self.color0
        if self.DegatSubit == 1:
            self.Image = self.color1
        elif self.DegatSubit == 2:
            self.Image = self.color2
        elif self.DegatSubit == 3:
            self.Image = self.color3
        elif self.DegatSubit == 4:
            self.Image = self.color4

        self.PixelArt = pCanevas.create_rectangle(0, 0, 100, 100, fill=self.color0, outline = 'black')
        pCanevas.itemconfig(self.imageOnCanvas, image=self.PixelArt)