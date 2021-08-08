from PyQt5 import uic
from PyQt5.QtWidgets import QDialogButtonBox, QDialog, QFileDialog

from src.data_management.database.io.SourceIO import SourceIO
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
        source = Source(-1, self.name.text(), self.description.toPlainText(), self.path.text())
        try:
            self.source_io.insert(source)
        # TODO Move exception handling to io and create custom exceptions with logs
        except Exception:
            pass

    def cancel(self):
        pass
