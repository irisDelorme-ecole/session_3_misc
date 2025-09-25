from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QWidget, QApplication
from PyQt6.uic import loadUi
import sys


class Ex2(QWidget):

    label:QLabel
    button:QPushButton
    __num_click:int = 0

    def __init__(self):

        super().__init__()
        loadUi("ex2.ui", self)

        self.button.clicked.connect(self.on_click)

    def on_click(self):
        self.__num_click += 1
        self.label.setText(f"Vous avez cliqué {self.__num_click} fois.")

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    ex2 = Ex2()
    ex2.show()
    sys.exit(app.exec())

    #complet