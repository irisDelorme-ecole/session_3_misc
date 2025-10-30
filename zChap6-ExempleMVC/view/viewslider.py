from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QSlider, QVBoxLayout


class ViewSlider(QWidget):
    __slider : QSlider

    def __init__(self):
        super().__init__()

        self.__slider = QSlider(Qt.Orientation.Horizontal)
        self.__slider.setRange(-10,10)

        layout = QVBoxLayout()
        layout.addWidget(self.__slider)
        self.setLayout(layout)
        self.show()

    def set_position(self, value):
        self.__slider.setValue(value)

    @property
    def slider(self):
        return self.__slider

