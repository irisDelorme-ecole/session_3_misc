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

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self,value):
        self._value = value
        self.valueChanged.emit(self._value)