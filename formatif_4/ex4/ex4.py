from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QWidget, QApplication, QTextEdit, QLineEdit, QComboBox, \
    QRadioButton, QCheckBox
from PyQt6.uic import loadUi
import sys


class Ex4(QWidget):

    lineEdit : QLineEdit
    comboBox : QComboBox
    option1Button : QRadioButton
    option2Button : QRadioButton
    option3Button : QRadioButton
    checkBox : QCheckBox

    def __init__(self):
        super().__init__()

        loadUi("ex4.ui",self)

        self.lineEdit.setEnabled(False)

        self.checkBox.checkStateChanged.connect(lambda state: self.lineEdit.setEnabled(state == Qt.CheckState.Checked))

        self.comboBox.addItems(["option 1", "option 2", "option 3"])

        self.comboBox.currentTextChanged.connect(lambda text : self.which_button(text))


    def which_button(self, text):
        if text == "option 1":
            self.option1Button.click()

        elif text == "option 2":
            self.option2Button.click()

        else:
            self.option3Button.click()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex4 = Ex4()
    ex4.show()
    sys.exit(app.exec())
    #complet
