from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton
from src.DataManagement.IO.SourceIO import SourceIO

# TODO Show origin in combo box
# TODO Add cancel button
# TODO Add New origin/source btn


class SourceSelectionDialog(QDialog):
    def __init__(self, requiredSources):
        super(SourceSelectionDialog, self).__init__()

        self.availableSources = SourceIO().getAll()
        self.availableSourcesStrings = [s.toOriginNameRepr() for s in self.availableSources]
        self.requiredSources = requiredSources
        self.sources = [self.availableSources[0] for _ in range(len(self.requiredSources))]

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
        comboBox.addItems(self.availableSourcesStrings)

        comboBox.currentIndexChanged.connect(lambda i: self.setSource(i, index))
        layout.addWidget(label)
        layout.addWidget(comboBox)

        return layout

    def finishButtonClicked(self):
        self.accept()

    def setSource(self, comboBoxSelectionIndex, widgetSourceIndex):
        self.sources[widgetSourceIndex] = self.availableSources[comboBoxSelectionIndex]