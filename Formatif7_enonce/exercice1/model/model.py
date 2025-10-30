from PyQt6.QtCore import QAbstractListModel, Qt, QModelIndex


class TasksModel(QAbstractListModel):
    __tasks:dict[str,bool]

    def __init__(self):

        super().__init__()
        self.__tasks={"tache 1":True, "tache 2": False,"autre tache" :False }

    def data(self, index, role):
        if not index.isValid():
            return None
        task = self.__tasks[index.row()]#TODO: make work
        if role == Qt.ItemDataRole.DisplayRole:
            return task.__str__()
        elif role == Qt.ItemDataRole.UserRole:
            return task
        elif role == Qt.ItemDataRole.ToolTipRole:
            return task.marque
        return None

    def rowCount(self, parent=QModelIndex()):  # what
        return len(self.__tasks)

    def addItem(self, item):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.__tasks.append(item)#TODO: make work
        self.endInsertRows()