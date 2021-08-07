from PyQt5 import uic
from PyQt5.QtWidgets import QDialogButtonBox, QDialog

from src.data_management.database.io.SourceIO import SourceIO


class SourceAddDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.source_io = SourceIO()
        self.set_up_ui()

    def set_up_ui(self):
        uic.loadUi('res/layout/source_add_dialog.ui', self)
        self.name.textChanged.connect(self.data_changed)
        self.description.textChanged.connect(self.data_changed)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.ok)
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.cancel)

    def data_changed(self):
        if self.name.text() != '' and self.description.toPlainText() != '' and self.path.text() != '':
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)

    def ok(self):
        pass

    def cancel(self):
        pass
