from PyQt6.QtCore import QObject, pyqtSignal

class CounterModel(QObject):
    valueChanged = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self._value = 0

    def increment(self):
        self._value += 1
        self.valueChanged.emit(self._value)

    def decrement(self):
        self._value -= 1
        self.valueChanged.emit(self._value)

    def value(self):
        return self._value