from PyQt6.QtGui import QColor, QAction
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QCheckBox, QPushButton, QVBoxLayout, QWidget, \
    QColorDialog, QMenu
from PyQt6.uic import loadUi
import sympy as sp
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib_canvas import MPLCanvas
from fonction_model import FonctionModel


class FonctionView(QMainWindow):
    fonctionLineEdit: QLineEdit
    titreLineEdit: QLineEdit
    afficherGrilleCheckBox: QCheckBox
    afficherPushButton: QPushButton
    plotWidget: QWidget
    menuGraphique: QMenu
    couleurAction: QAction

    def __init__(self):
        super().__init__()

        loadUi("ui/formatif5.ui", self)

        # setup de base
        self.fonction = FonctionModel()
        self.canvas = MPLCanvas(self.fonction)
        self.toolbar = NavigationToolbar(self.canvas)
        layout = QVBoxLayout(self.plotWidget)
        layout.addWidget(self.toolbar)
        self.plotWidget.layout().addWidget(self.canvas)

        self.afficherPushButton.setEnabled(False)
        self.couleurAction.triggered.connect(self.set_colour)

        self.afficherGrilleCheckBox.checkStateChanged.connect(self.fonction.set_has_grille)

        if not self.titreLineEdit.text().strip() and not self.fonctionLineEdit.text().strip():
            self.afficherPushButton.setEnabled(True)
            self.afficherPushButton.clicked.connect(self.set_fonction)

    def set_colour(self):
        self.fonction.set_colour(QColorDialog.getColor().name())

    def set_fonction(self):
        fonction = sp.sympify(self.fonctionLineEdit.text())

        self.fonction.set_titre(self.titreLineEdit.text())
        self.fonction.set_fonction(fonction)
        #self.canvas.plot()
        self.plotWidget.layout().addWidget(self.canvas)
