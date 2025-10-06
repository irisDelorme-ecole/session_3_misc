import sys
from fonction_view import FonctionView
from PyQt6.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex3 = FonctionView()
    ex3.show()
    sys.exit(app.exec())