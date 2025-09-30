import numpy as np
import sympy as sp

class FonctionModel():

    titre:str

    def __init__(self, fonction, titre):
        self.titre = titre
        self.fonction = fonction


    def get_fonction(self):
        x = sp.symbols('x')
        return sp.lambdify(x, self.fonction, 'numpy')


    def get_titre(self):
        return self.titre


