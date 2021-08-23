from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QLabel, QComboBox, QDialogButtonBox, QWidget

from src.data_management.database.io.KeyIO import KeyIO
from src.data_management.database.io.SourceIO import SourceIO


class KeySelectionDialog(QDialog):
    def __init__(self, required_keys):
        super(KeySelectionDialog, self).__init__()
        self.available_keys = KeyIO().get_all()
        self.required_keys = required_keys
        self.selected_keys = [None for _ in range(len(required_keys))]
        self.set_up_ui()

    def set_up_ui(self):
        uic.loadUi('res/layout/key_selection_dialog.ui', self)
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.ok)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.cancel)
        # Add selection
        for i, (name, dimension) in enumerate(self.required_keys):
            selection_layout = self.key_selector_layout(i, name, dimension)
            self.selection_layout.addLayout(selection_layout)

    def ok(self):
        if all(map(lambda x: x != "None" and x is not None, self.selected_keys)):
            self.accept()

    def cancel(self):
        self.close()

    def key_selector_layout(self, index, name, dimension) -> QWidget:
        layout = QHBoxLayout()
        label = QLabel(name)
        combo_box = QComboBox()
        # TODO Remove Empty ("") after first selection
        keys_with_dimension = [key for key in self.available_keys if key.dimension == dimension]
        combo_box.addItems(["None"] + [f'{key.source}: {key.name}' for key in keys_with_dimension])
        combo_box.currentIndexChanged.connect(lambda i: self.set_key(i - 1, index))
        layout.addWidget(label)
        layout.addWidget(combo_box)
        return layout

    def set_key(self, combo_box_selection_index: int, widget_key_index: int) -> None:
        self.selected_keys[widget_key_index] = self.available_keys[combo_box_selection_index]
        if all(map(lambda x: x != "None" and x is not None, self.selected_keys)):
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)