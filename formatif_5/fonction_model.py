import numpy as np
import sympy as sp

class FonctionModel():

    titre:str
    has_grille: bool = False

    def __init__(self):
        self.titre = "titre"
        self.fonction = " "

    def set_has_grille(self):
        self.has_grille = (self.has_grille != True)

    def get_has_grille(self):
        return self.has_grille

    def set_titre(self, value):
        self.titre = value

    def set_fonction(self,value):
        self.fonction = value

    def get_fonction(self):
        x = sp.symbols('x')
        return sp.lambdify(x, self.fonction, 'numpy')


    def get_titre(self):
        return self.titre


