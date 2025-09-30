from PyQt6.QtWidgets import QMainWindow, QLineEdit, QCheckBox, QPushButton, QApplication, QVBoxLayout, QWidget
from PyQt6.uic import loadUi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sympy as sp
import numpy as np
import sys
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure

from matplotlib_canvas import MPLCanvas
from fonction_model import FonctionModel

class FonctionView(QMainWindow):

    fonctionLineEdit:QLineEdit
    titreLineEdit:QLineEdit
    afficherGrilleCheckBox:QCheckBox
    afficherPushButton:QPushButton
    plotWidget:QWidget


    def __init__(self):
        super().__init__()


        loadUi("ui/formatif5.ui", self)



        self.canvas = MPLCanvas()
      



        if self.titreLineEdit.textChanged and self.fonctionLineEdit.textChanged:
            self.afficherPushButton.clicked.connect(self.set_fonction)


    def set_fonction(self):
        fonction = sp.sympify(self.fonctionLineEdit.text())

        self.fonction = FonctionModel(fonction,self.titreLineEdit.text())
        self.canvas.plot(self.fonction.get_fonction())
        self.canvas.set_titre(self.fonction.get_titre())
        self.imbriquer()

    def imbriquer(self):
        self.toolbar = NavigationToolbar(self.canvas)
        layout = QVBoxLayout(self.plotWidget)  # 'plot_widget' is a placeholder widget in the .ui file
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex3 = FonctionView()
    ex3.show()
    sys.exit(app.exec())