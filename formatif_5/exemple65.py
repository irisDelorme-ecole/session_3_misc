import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np

class MPLCanvas(FigureCanvas):
    def __init__(self):
        # Création de la figure matplotlib self. fig, self. ax = plt.subplots()
        self.__fig, self.__ax = plt.subplots()
        #appel du constructuer de FigureCanvas avec la fig créée en parametre
        super().__init__(self.__fig)
        self.plot()

    def plot(self):
        #Add specific code to the canvas!
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        self.__ax.plot(x, y)
        self.__ax.set_title("Exemple Sin(x)")

class FenetreGraph(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Graphique Matplotlib dans Qt")
        # Widget central
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout()
        central.setLayout(layout)
        #Canvas Qt pour matplotlib
        canvas = MPLCanvas()
        layout.addWidget(canvas)
        toolbar = NavigationToolbar(canvas, self)
        layout.addWidget(toolbar)

if  __name__  == "__main__":
    app = QApplication(sys.argv)
    fen = FenetreGraph()
    fen.show()
    sys.exit(app.exec())
