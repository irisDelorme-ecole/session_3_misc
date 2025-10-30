from PyQt6.QtWidgets import QMainWindow, QListView
from PyQt6.uic import loadUi


class TasksView(QMainWindow):
    tasksListView:QListView
    def __init__(self):
        super().__init__()
        loadUi("view/ui/tasksView.ui", self)