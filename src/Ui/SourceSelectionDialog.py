from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QLabel, QComboBox, QDialogButtonBox, QWidget

from src.data_management.database.io.SourceIO import SourceIO


class SourceSelectionDialog(QDialog):
    def __init__(self, required_sources):
        super(SourceSelectionDialog, self).__init__()
        # Sources usable for widget data
        self.available_sources = SourceIO().get_all()
        # Sources needed for widget
        self.required_sources = required_sources
        self.selected_sources = [None for _ in required_sources]
        self.set_up_ui()

    def set_up_ui(self):
        uic.loadUi('res/layout/source_selection_dialog.ui', self)
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.ok)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.cancel)
        # Add selection
        for i, source in enumerate(self.required_sources):
            selection_layout = self.source_selector_layout(i, source)
            self.selection_layout.addLayout(selection_layout)

    def ok(self):
        # TODO Add Hint that says something like "U have to specify more sources."
        print('ssd-ok')
        if all(map(lambda x: x != "None" and x is not None, self.selected_sources)):
            self.accept()

    def cancel(self):
        self.close()

    def source_selector_layout(self, index, source) -> QWidget:
        layout = QHBoxLayout()
        label = QLabel(source)
        combo_box = QComboBox()
        # TODO Remove Empty ("") after first selection
        combo_box.addItems(["None"] + [s.__repr__() for s in self.available_sources])
        combo_box.currentIndexChanged.connect(lambda i: self.set_source(i-1, index))
        layout.addWidget(label)
        layout.addWidget(combo_box)
        return layout

    def set_source(self, combo_box_selection_index: int, widget_source_index: int) -> None:
        self.selected_sources[widget_source_index] = self.available_sources[combo_box_selection_index]
        # Enable ok btn if all sources set
        if all(map(lambda x: x != "None" and x is not None, self.selected_sources)):
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)