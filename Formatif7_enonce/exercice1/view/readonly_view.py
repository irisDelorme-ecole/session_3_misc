from PyQt6.QtWidgets import QWidget, QLabel, QPushButton
from PyQt6.uic import loadUi


class TasksReadOnlyView(QWidget):


    def __init__(self):
        super().__init__()
        loadUi("view/ui/tasksReadOnlyView.ui", self)

    def update_label(self,nb_total, nb_faites):
        self.label.setText(f'Nombre de taches : {nb_total} dont {nb_faites} sont effectuées')