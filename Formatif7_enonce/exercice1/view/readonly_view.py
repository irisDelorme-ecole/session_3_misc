from PyQt6.QtWidgets import QWidget, QLabel, QPushButton
from PyQt6.uic import loadUi


class TasksReadOnlyView(QWidget):


    def __init__(self):
        super().__init__()
        loadUi("view/ui/tasksReadOnlyView.ui", self)