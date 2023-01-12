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
        self.Image0 = 'Protection{}-D0.gif'.format(pNumero) #Permet d'afficher chacune des 5 textures correspondant au dégats subbits
        self.Image1 = 'Protection{}-D1.gif'.format(pNumero)
        self.Image2 = 'Protection{}-D2.gif'.format(pNumero)
        self.Image3 = 'Protection{}-D3.gif'.format(pNumero)
        self.Image4 = 'Protection{}-D4.gif'.format(pNumero)
        self.DegatSubit = 0

        # si tu veux les dessiner mais galère de faire des trou, peut être faire des carrés plus petit ?
        # create_rectangle(0, 0, 100, 100, fill="blue", outline = 'blue')
        self.PixelArt = PhotoImage(master=pWindow,
                                   file='PixelArts/Protections/' + self.Image0)
        self.imageOnCanvas = pCanevas.create_image(self.Position[0], self.Position[1],
                                                   image=self.PixelArt) #Affichage sur le canevas

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
            self.Image = self.Image0
        if self.DegatSubit == 1:
            self.Image = self.Image1
        elif self.DegatSubit == 2:
            self.Image = self.Image2
        elif self.DegatSubit == 3:
            self.Image = self.Image3
        elif self.DegatSubit == 4:
            self.Image = self.Image4

        self.PixelArt = PhotoImage(master=pWindow,
                                   file='PixelArts/Protections/' + self.Image)
        pCanevas.itemconfig(self.imageOnCanvas, image=self.PixelArt)