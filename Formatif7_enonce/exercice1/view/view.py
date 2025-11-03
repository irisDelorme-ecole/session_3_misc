from PyQt6.QtCore import pyqtSignal, QModelIndex, Qt
from PyQt6.QtWidgets import QMainWindow, QListView, QPushButton, QVBoxLayout, QDialog, QLineEdit, QDialogButtonBox
from PyQt6.uic import loadUi


class TasksView(QMainWindow):
    tasksListView:QListView
    ajouterPushButton : QPushButton
    updated = pyqtSignal(QModelIndex)

    def __init__(self):
        super().__init__()
        loadUi("view/ui/tasksView.ui", self)

        self.tasksListView.doubleClicked.connect(self.updated.emit)
        self.ajouterPushButton.clicked.connect(self.on_click)

    def on_click(self):
        # buttons = QDialogButtonBox()
        # buttons.addButton(QDialogButtonBox.StandardButton.Save)
        # buttons.addButton(QDialogButtonBox.StandardButton.Cancel)
        box = QDialog()
        # box.addWidget(buttons)
        box.setWindowModality(Qt.WindowModality.ApplicationModal)
        box.exec()


    def set_model(self, model):
        self.tasksListView.setModel(model)


