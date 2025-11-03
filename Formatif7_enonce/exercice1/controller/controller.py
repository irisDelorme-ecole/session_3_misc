

class TasksController:

    def __init__(self, model, view,readonly_view):
        self.model = model
        self.view = view
        self.view_read_only = readonly_view

        self.view.set_model(self.model)
        self.view.updated.connect(self.model.change_state)

        self.model.updated.connect(self.view_read_only.update_label)



