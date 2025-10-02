import sympy as sp
from PyQt6.QtCore import QObject, pyqtSlot, pyqtSignal

class FonctionModel(QObject):
    has_updated = pyqtSignal(str)
    __titre:str
    __has_grille: bool = False
    __couleur:str
    __fonction:str




    def __init__(self):
        super().__init__()
        self.__titre = "titre"
        self.__fonction = " "
        self.__couleur = "000000"


    def get_colour(self):
        return self.__couleur

    def set_colour(self, value):
        self.__couleur = value
        self.has_updated.emit("is triggered")
        # emit

    def set_has_grille(self):
        self.__has_grille = (self.__has_grille != True)
        #emit

    def get_has_grille(self):
        return self.__has_grille

    def set_titre(self, value):
        self.__titre = value
        #emit

    def set_fonction(self,value):
        self.__fonction = value
        self.has_updated.emit("is triggered")
        #emit

    def get_fonction(self):
        x = sp.symbols('x')
        return sp.lambdify(x, self.__fonction, 'numpy')


    def get_titre(self):
        return self.__titre


