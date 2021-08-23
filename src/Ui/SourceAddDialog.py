import importlib

from PyQt5 import uic
from PyQt5.QtWidgets import QDialogButtonBox, QDialog, QFileDialog

from src.data_management.database.io.KeyIO import KeyIO
from src.data_management.database.io.SourceIO import SourceIO
from src.data_management.dto.Key import Key
from src.data_management.dto.Source import Source


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
        self.path_button.clicked.connect(self.get_python_script)

    def data_changed(self):
        if self.name.text() != '' and self.description.toPlainText() != '' and self.path.text() != '':
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)

    # TODO Button looks sh**
    def get_python_script(self):
        file_path = QFileDialog().getOpenFileUrl(self, 'Select Python Script', filter='Python Files (*.py)')
        if file_path[1] != '':
            self.path.setText(file_path[0].path())

    def ok(self):
        script = importlib.import_module('scripts.default.' + 'Random.Random')#self.path.text().split('/')[-2])
        keys = script.provides
        key_io = KeyIO()
        source = Source(-1, self.name.text(), self.description.toPlainText(), self.path.text())
        self.source_io.insert(source)
        source_id = self.source_io.get_last_id()
        for name, dimension in keys:
            key = Key(-1, name, source_id, dimension)
            key_io.insert(key)
        # TODO Move exception handling to io and create custom exceptions with logs


    def cancel(self):
        pass
