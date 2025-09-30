import numpy as np
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import sympy as sp
from fonction_model import FonctionModel


class MPLCanvas(FigureCanvas):

#makes a mpl plot.

    def __init__(self, fonction_model):
        self.__fig, self.__axe = plt.subplots()
        self.__fonction_model = fonction_model
        super().__init__(self.__fig)
        plt.draw()#makes blank plot with axes visible


    def plot(self, has_grille):
        self.__axe.clear()
        f = self.__fonction_model.get_fonction()
        x = np.linspace(0,10,100)
        self.__axe.plot(x, f(x))
        self.__axe.grid(has_grille)
        plt.title(self.__fonction_model.get_titre())
        plt.draw()



