from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class MPLCanvas(FigureCanvas):



    def __init__(self):
        self.__fig, self.__axe = plt.subplots()

        super().__init__(self.__fig)

        self.plot()

    def plot(self):
        #TODO make it read funct
        #
        #fonction = sp.lambdify(variable, f, 'numpy')

