from PyQt5 import uic
from PyQt5.QtWidgets import QDialogButtonBox, QDialog


class SourceAddDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.set_up_ui()

    def set_up_ui(self):
        uic.loadUi('res/layout/source_add_dialog.ui', self)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.ok)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.cancel)

    def ok(self):
        pass

    def cancel(self):
        pass
