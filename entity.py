# -*- coding: utf-8 -*-

# %%----------------------Import----------------------------------------------#

from tkinter import PhotoImage

class Entity:
    """Classe qui défini toutes les Entitys du jeu"""

    def __init__(self, pPositionInitiale):
        """
        Méthode de création d'une Entity. Elle a pour parametre
        pPositionInitiale soit une liste de 2 entiers
        Parameters
        ----------
        pPositionInitiale : Liste de taille 2 contenant 2 entiers/int
            Contient les coordonnées de l'Entity. Elle permet de le positionner
            sur le canvas.
            
        Returns
        -------
        None.
        """

        self.Position = pPositionInitiale

    def getPos(self):
        """
        Méthode getteur pour récuperer la position de l'Entity
        
        Returns
        -------
         Liste de taille 2 contenant 2 entiers/int
            Coordonnées de l'Entity en X et Y
        """

        return self.Position
