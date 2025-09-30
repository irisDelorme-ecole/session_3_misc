import numpy as np
import sympy as sp

class FonctionModel():

    titre:str

    def __init__(self):
        self.titre = "titre"
        self.fonction = " "

    def set_titre(self, value):
        self.titre = value

    def set_fonction(self,value):
        self.fonction = value

    def get_fonction(self):
        x = sp.symbols('x')
        return sp.lambdify(x, self.fonction, 'numpy')


    def get_titre(self):
        return self.titre


