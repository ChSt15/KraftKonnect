from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QLabel, QComboBox, QDialogButtonBox, QWidget

from src.data_management.database.io.KeyIO import KeyIO
from src.data_management.database.io.SourceIO import SourceIO


class KeySelectionDialog(QDialog):
    def __init__(self, required_keys):
        super(KeySelectionDialog, self).__init__()
        self.available_keys = KeyIO().get_all()
        self.required_keys = required_keys
        self.selected_keys = [None for _ in required_keys]
        self.sources = {source.id: source.name for source in SourceIO().get_all()}
        self.set_up_ui()

    def set_up_ui(self):
        uic.loadUi('res/layout/key_selection_dialog.ui', self)
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.ok)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.cancel)
        # Add selection
        for i, source in enumerate(self.required_keys):
            selection_layout = self.key_selector_layout(i, source)
            self.selection_layout.addLayout(selection_layout)

    def ok(self):
        # TODO Add Hint that says something like "U have to specify more sources."
        print('ssd-ok')
        if all(map(lambda x: x != "None" and x is not None, self.selected_keys)):
            self.accept()

    def cancel(self):
        self.close()

    def key_selector_layout(self, index, source) -> QWidget:
        layout = QHBoxLayout()
        label = QLabel(source)
        combo_box = QComboBox()
        # TODO Remove Empty ("") after first selection
        combo_box.addItems(["None"] + [f'{self.sources[key.source]}: {key.name}' for key in self.available_keys])
        combo_box.currentIndexChanged.connect(lambda i: self.set_key(i - 1, index))
        layout.addWidget(label)
        layout.addWidget(combo_box)
        return layout

    def set_key(self, combo_box_selection_index: int, widget_key_index: int) -> None:
        self.selected_keys[widget_key_index] = self.available_keys[combo_box_selection_index]
        if all(map(lambda x: x != "None" and x is not None, self.selected_keys)):
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)