import sys
import traceback
from time import sleep

from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QProgressBar
from PyQt6.uic import loadUi

class longWorkThread(QThread):
    signal = pyqtSignal(int)

    def __init__(self,stop):
        super().__init__()
        self.stop = stop

    def run(self):

        progress = 1
        while not self.stop :
            sleep(1)
            self.signal.emit(progress)
            progress+=1



class View(QMainWindow):
    progressLabel:QLabel
    startPushButton:QPushButton
    stopPushButton:QPushButton
    progressBar:QProgressBar
    stop:bool

    def __init__(self):
        super().__init__()
        loadUi("ui/view.ui", self)
        self.stopPushButton.clicked.connect(self.stop)
        self.startPushButton.clicked.connect(self.lancer_thread)
        self.stop = True

    def lancer_thread(self):
        self.stop = False
        self.thread = longWorkThread(self.stop)

        self.thread.start()

        self.thread.signal.connect(self.update_progress)



    def stop(self):
        self.stop = True
        self.progressLabel.setText("finished")

    def update_progress(self,value):
        self.progressLabel.setText(f"Processed {value} jobs")
        self.progressBar.setValue(value)

    # def simulate_long_work(self):
    #     self.stop=False
    #     progress = 1
    #     while not self.stop :
    #         sleep(1)
    #         self.progressLabel.setText(f"Processed {progress} jobs")
    #         progress+=1

    def stop_long_work(self):
        self.stop = True
        self.progressLabel.setText(f"End Jobs")

def qt_exception_hook(exctype, value, tb):
    traceback.print_exception(exctype, value, tb)

if __name__ == "__main__":
    sys.excepthook = qt_exception_hook
    app = QApplication(sys.argv)

    view = View()
    view.show()

    sys.exit(app.exec())
