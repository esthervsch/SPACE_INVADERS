# -*- coding: utf-8 -*-


# %%----------------------Import----------------------------------------------#

from tkinter import PhotoImage
import math, random
from entity import Entity


class EntityTirEnnemi(Entity):
    """Sous-classe pour les tirs des aliens"""

    def afficherTirEnnemi(self, pCanevas,):
        """
        Méthode d'affichage des Entités. Les parametres pWindow et pCanevas
        sont respectivement la fenêtre et le canvas.
        
        Parameters
        ----------
        pCanevas : tkinter canevas
            On choisit le canevas
        Returns
        -------
        None.
        """

        pCanevas.create_rectangle(0, 0, 10, 100, fill='red', outline = 'black')
        #faire un deuxième rectangle pour montrer une transition peut être intéressant via un paramètre ?

    def hitbox2(self, pPositionJoueur, pTirPosition):
        """
        Méthode pour les hitbox du joueur. Permet de savoir si le joueur est
        touché par un tir

        Parameters
        ----------
        pPositionJoueur : Liste
            Liste de 2 entiers, renseigne les coordonnées du joueur.
        pTirPosition : Liste
             Liste de 2 entiers, renseigne les coordonnées du projectile alien.
             
        Returns
        -------
        bool
            True si le projectile a touché le joueur.
            False sinon.
        """

        distance = math.sqrt((pPositionJoueur[0] - pTirPosition[0]) ** 2 +
                             (pPositionJoueur[1] - pTirPosition[1]) ** 2)
        if distance <= 25:
            return True
        else:
            return False