
from model.ex74_model import CounterModel
from view.ex74_view import CounterView
from view.viewslider import ViewSlider


class CounterController:
    model:CounterModel
    view:CounterView
    viewSlider:ViewSlider

    def __init__(self, model, view, viewSlider):
        self.model = model
        self.view = view
        self.viewSlider = viewSlider

        # Connexions
        self.view.plusPushButton.clicked.connect(self.increment)
        self.view.minusPushButton.clicked.connect(self.decrement)
        self.model.valueChanged.connect(self.update_value)
        self.viewSlider.slider.valueChanged.connect(self.update_value)

        # Initialisation
        self.update_value(self.model.value())


    def increment(self):
        self.model.increment()


    def decrement(self):
        self.model.decrement()


    def update_value(self, value):
        self.view.valueLabel.setText(str(value))
        self.viewSlider.set_position(value)
        self.model.value = value
