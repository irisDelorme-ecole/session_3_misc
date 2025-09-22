# import sys
# from PyQt6.QtWidgets import QApplication, QWidget
#
# app = QApplication(sys.argv)
# fenetre = QWidget()
# fenetre.setWindowTitle("Ma première fenêtre Qt")
# fenetre.resize(300, 200)
# fenetre.show()
# sys.exit(app.exec())#ecoute interactions utilisateurs

from PyQt6.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget,QPushButton , QLabel
import sys
app = QApplication(sys.argv)
fenetre = QWidget()
fenetre.setWindowTitle("Fenêtre à 3 composants")

def affich_bonj():
    label.setText(f'bonjour ' + champ.text() + '.')

champ = QLineEdit()

champ.setPlaceholderText("Entrez votre nom")

bouton = QPushButton()
bouton.setText("Cliquez!!")
label = QLabel()
label.setText("Bonjour ....")

layout = QHBoxLayout()

bouton.clicked.connect(affich_bonj)#yipee

def on_change(value):
    label.setText(f'Bonjour {value}, bienvenue dans cette application graphique')
champ.textChanged.connect(on_change)

layout.addWidget(champ)
layout.addWidget(bouton)
layout.addWidget(label)
fenetre.setLayout(layout)
fenetre.resize(300, 200)
fenetre.show()
sys.exit(app.exec())