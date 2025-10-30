import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QGridLayout
from PyQt6.uic import loadUi

class FenetreExercice5(QMainWindow):
    gridLayout : QGridLayout
    labelCoordonnees : QLabel
    label : QLabel

    def __init__(self):
        super().__init__()
        loadUi("ui/exercice5.ui", self)

        self.newLabel = MonLabel(self)
        self.gridLayout.replaceWidget(self.label, self.newLabel)
        self.newLabel.setText("cliquez ici")



    def set(self,text):
        self.labelCoordonnees.setText(text)

    def keyPressEvent(self, ev):
        if ev.key() == Qt.Key.Key_Delete:
            self.labelCoordonnees.setText("on a appuiyé sur delete.")




class MonLabel(QLabel):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setStyleSheet("background-color: lightgray;")
        self.setText("cliquez ici")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def mousePressEvent(self, ev):
       self.parent.set(f"On a cliquez à ({ev.position().x()},{ev.position().y()})")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = FenetreExercice5()
    fenetre.show()
    sys.exit(app.exec())
