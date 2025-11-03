from PyQt6.QtWidgets import QWidget, QLabel, QPushButton
from PyQt6.uic import loadUi



class CounterView(QWidget):

    valueLabel:QLabel
    minusPushButton: QPushButton
    plusPushButton:QPushButton


    def __init__(self):
        super().__init__()
        loadUi("view/ui/counter.ui", self)


    @property
    def controller(self):
        return self.__controller
    
    @controller.setter
    def controller (self, value):
        self.__controller=value

    def toto(self):
        self.__controller
