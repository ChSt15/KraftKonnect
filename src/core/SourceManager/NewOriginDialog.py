from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QComboBox, QLabel
from src.core.SourceManager.OriginTypes import OriginTypes
from src.DataManagement.IO.OriginIO import OriginIO

class NewOriginDialog(QDialog):
    def __init__(self):
        super(NewOriginDialog, self).__init__()

        self.nextId = OriginIO().getHighestID()+1

        # Layout
        self.layout = QVBoxLayout()
        self.setMinimumSize(640, 420)

        # Type selection
        typeSelectionLayout = QHBoxLayout()
        typeLabel = QLabel('How to fetch data from origin:')
        self.typeComboBox = QComboBox()
        for t in OriginTypes:
            self.typeComboBox.addItem(t.name)
        typeSelectionLayout.addWidget(typeLabel)
        typeSelectionLayout.addWidget(self.typeComboBox)

        self.layout.addLayout(typeSelectionLayout)
        self.setLayout(self.layout)
