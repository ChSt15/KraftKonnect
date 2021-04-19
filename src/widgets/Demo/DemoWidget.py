from PyQt5.QtWidgets import QWidget
class DemoWidget(QWidget):

    requiredSources = ["FirstName", "SecondName"]

    def __init__(self):
        super(DemoWidget, self).__init__()

    def update(self, *data) -> None:
        # Update widget
        pass