from PyQt6.QtWidgets import QMainWindow, QLineEdit, QCheckBox, QPushButton, QApplication, QVBoxLayout, QWidget, \
    QColorDialog
from PyQt6.uic import loadUi
import sympy as sp
import sys
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
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

        # setup de base
        self.colourPicker = QColorDialog()
        self.colourPicker.setOption(QColorDialog.ColorDialogOption.NoButtons)

        self.plotWidget = QWidget()

        self.fonction = FonctionModel()
        self.canvas = MPLCanvas(self.fonction)
        self.toolbar = NavigationToolbar(self.canvas)
        layout = QVBoxLayout(self.plotWidget)
        layout.addWidget(self.toolbar)
        self.plotWidget.layout().addWidget(self.canvas)

        self.tabWidget.addTab(self.plotWidget, "Graphique")

        self.tabWidget.addTab(self.colourPicker, "Couleur")
        self.colour = "black"


        self.afficherPushButton.setEnabled(False)


        if self.titreLineEdit.textChanged and self.fonctionLineEdit.textChanged:
            self.afficherPushButton.setEnabled(True)
            self.afficherPushButton.clicked.connect(self.set_fonction)




    def set_colour(self):
        self.colour = self.colourPicker.selectedColor().name()

    def set_fonction(self):
        fonction = sp.sympify(self.fonctionLineEdit.text())

        self.fonction.set_titre(self.titreLineEdit.text())
        self.fonction.set_fonction(fonction)
        self.canvas.plot(self.afficherGrilleCheckBox.isChecked(), self.colourPicker.currentColor().name())
        self.plotWidget.layout().addWidget(self.canvas)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex3 = FonctionView()
    ex3.show()
    sys.exit(app.exec())