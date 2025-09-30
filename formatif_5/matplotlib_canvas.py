import numpy as np
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class MPLCanvas(FigureCanvas):



    def __init__(self):
        self.__fig, self.__axe = plt.subplots()

        super().__init__(self.__fig)

    def set_titre(self, value):
        plt.title(value)

    def plot(self, fonction):
        x = np.linspace(0,10,100)
        self.__axe.plot(x, fonction(x))



