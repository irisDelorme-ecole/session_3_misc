from PyQt6.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget,QPushButton , QLabel
import sys



class Fenetre(QWidget):

    def __init__(self):
        super().__init__()
        self.label = QLabel()
        self.label.setText("Salut")

        self.bouton = QPushButton()
        self.bouton.setText("cliquez")

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.bouton)
        self.setLayout(self.layout)
        self.resize(300, 200)
        self.times = 0
        self.bouton.clicked.connect(self.on_click)

    def on_click(self):
        self.times += 1
        self.label.setText("Vous avez cliqué " + str(self.times) + " fois.")


app = QApplication(sys.argv)
fenetre = Fenetre()

fenetre.show()
sys.exit(app.exec())