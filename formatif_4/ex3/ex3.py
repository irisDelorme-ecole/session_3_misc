from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QWidget, QApplication, QTextEdit, QLineEdit
from PyQt6.uic import loadUi
import sys

class Ex3(QWidget):

    label : QLabel
    pushButton : QPushButton
    textEdit : QTextEdit
    lineEdit : QLineEdit

    def __init__(self):
        super().__init__()
        loadUi("ex3.ui",self)

        self.pushButton.clicked.connect(self.concat)


    def concat(self):
        self.label.setText(self.lineEdit.text() + self.textEdit.toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex3 = Ex3()
    ex3.show()
    sys.exit(app.exec())
    #complet

