from PyQt6.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget,QPushButton , QLabel, QMainWindow
import sys

from PyQt6.uic import loadUi


class Fenetre(QWidget):



    def __init__(self):
        super().__init__()
        loadUi("test.ui",self)


    def on_click(self):
        self.times += 1
        self.label.setText("Vous avez cliqué " + str(self.times) + " fois.")


app = QApplication(sys.argv)
fenetre = Fenetre()

fenetre.show()
sys.exit(app.exec())