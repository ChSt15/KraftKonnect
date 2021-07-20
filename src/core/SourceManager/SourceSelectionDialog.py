from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton
from src.DataManagement.IO.SourceIO import SourceIO

# TODO Show origin in combo box
# TODO Add cancel button
# TODO Add New origin/source btn


class SourceSelectionDialog(QDialog):
    def __init__(self, requiredSources):
        super(SourceSelectionDialog, self).__init__()

        # Sources usable for widget data
        self.availableSources = SourceIO().getAll()
        # Sources needed for widget
        self.requiredSources = requiredSources
        self.selectedSources = [None for _ in requiredSources]

        self.configureLayout()

        layout = QVBoxLayout()
        for i, source in enumerate(self.requiredSources):
            selectionLayout = self.sourceSelectorLayout(i, source)
            layout.addLayout(selectionLayout)

        finishButton = QPushButton('Create')
        finishButton.clicked.connect(self.finishButtonClicked)
        layout.addWidget(finishButton)

        self.setLayout(layout)


    def configureLayout(self):
        pass

    def sourceSelectorLayout(self, index, source):
        layout = QHBoxLayout()
        label = QLabel(source)
        comboBox = QComboBox()
        # TODO Remove Empty ("") after first selection
        comboBox.addItems([""] + [s.toOriginNameRepr() for s in self.availableSources])

        comboBox.currentIndexChanged.connect(lambda i: self.setSource(i-1, index))
        layout.addWidget(label)
        layout.addWidget(comboBox)

        return layout

    def finishButtonClicked(self):
        if not len(self.selectedSources) != len(self.requiredSources):
            self.accept()
        # TODO Add Hint that says something like "U have to specify more sources."

    def setSource(self, comboBoxSelectionIndex, widgetSourceIndex):
        self.selectedSources[widgetSourceIndex] = self.availableSources[comboBoxSelectionIndex]