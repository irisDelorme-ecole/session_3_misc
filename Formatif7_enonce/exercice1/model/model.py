from PyQt6.QtCore import QAbstractListModel, Qt, QModelIndex, pyqtSignal


class TasksModel(QAbstractListModel):
    __tasks:dict[str,bool]
    updated = pyqtSignal(int,int)

    updated_state = pyqtSignal(bool)

    def __init__(self):

        super().__init__()
        self.__tasks={"tache 1":True, "tache 2": False,"tache 3" :False }

    def data(self, index, role):

        if not index.isValid():
            return None
        task_keys = list(self.__tasks.keys())#TODO: make work
        task = task_keys[index.row()]
        if role == Qt.ItemDataRole.DisplayRole:

            if self.__tasks[task] == True:
                return f'{task} : effectuée'
            else:
                return f'{task} : à faire'
        if role == Qt.ItemDataRole.UserRole:
            return task
        return None

    def change_state(self, index):
        task = self.data(index, Qt.ItemDataRole.UserRole)
        bools = self.__tasks[task]

        self.__tasks[task] = not bools

    def rowCount(self, parent=QModelIndex()):  # what
        return len(self.__tasks)

    def nb_effectuees(self):
        vals = list(self.__tasks.values())
        nb = []
        for val in vals:
            if val:
                nb.append(val)

        return len(nb)

    def addItem(self, name, boolean):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.__tasks[name] = boolean#TODO: make work

        self.updated.emit(self.rowCount(), self.nb_effectuees())
        self.endInsertRows()