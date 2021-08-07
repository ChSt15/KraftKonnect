from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton
from src.DataManagement.IO.SourceIO import SourceIO

# TODO Show origin in combo box
# TODO Add cancel button
# TODO Add New origin/source btn


class SourceSelectionDialog(QDialog):
    def __init__(self, required_sources):
        super(SourceSelectionDialog, self).__init__()

        # Sources usable for widget data
        self.available_sources = SourceIO().get_all()
        # Sources needed for widget
        self.required_sources = required_sources
        self.selected_sources = [None for _ in required_sources]

        self.configure_layout()

        layout = QVBoxLayout()
        for i, source in enumerate(self.required_sources):
            selection_layout = self.source_selector_layout(i, source)
            layout.addLayout(selection_layout)

        finish_button = QPushButton('Create')
        finish_button.clicked.connect(self.finish_button_clicked)
        layout.addWidget(finish_button)

        self.setLayout(layout)


    def configure_layout(self):
        pass

    def source_selector_layout(self, index, source):
        layout = QHBoxLayout()
        label = QLabel(source)
        combo_box = QComboBox()
        # TODO Remove Empty ("") after first selection
        combo_box.addItems([""] + [s.__repr__() for s in self.available_sources])

        combo_box.currentIndexChanged.connect(lambda i: self.set_source(i-1, index))
        layout.addWidget(label)
        layout.addWidget(combo_box)

        return layout

    def finish_button_clicked(self):
        if not len(self.selected_sources) != len(self.required_sources):
            self.accept()
        # TODO Add Hint that says something like "U have to specify more sources."

    def set_source(self, combo_box_selection_index, widget_source_index):
        self.selected_sources[widget_source_index] = self.available_sources[combo_box_selection_index]