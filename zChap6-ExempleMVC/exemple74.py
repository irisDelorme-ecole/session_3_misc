import sys
import traceback

from PyQt6.QtWidgets import QApplication
from controller.ex74_controller import CounterController
from view.ex74_view import CounterView
from model.ex74_model import CounterModel
from view.viewslider import ViewSlider


def qt_exception_hook(exctype, value, tb):
    traceback.print_exception(exctype, value, tb)



if __name__ == "__main__":
    sys.excepthook = qt_exception_hook
    app = QApplication(sys.argv)

    model = CounterModel()
    view = CounterView()
    viewSlider = ViewSlider()
    controller = CounterController(model, view, viewSlider)
    view.controller = controller
    view.show()
    sys.exit(app.exec())
