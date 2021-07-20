from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QListWidget, QTableWidget, QPushButton, QLabel, QSplitter
from PyQt5.QtCore import Qt
from src.DataManagement.IO.DataIO import DataIO
from src.DataManagement.IO.SourceIO import SourceIO
from src.core.SourceManager.NewOriginDialog import NewOriginDialog


class SourceManagerDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('DataCollector Manager')
        self.originIo = OriginIO()
        self.sourceIo = SourceIO()
        self.origins = None

        # Left content
        leftLabel = QLabel('Origin')
        self.originList = QListWidget()
        leftContent = QVBoxLayout()
        leftContent.addWidget(leftLabel)
        leftContent.addWidget(self.originList)
        # Right content
        rightLabel = QLabel('Source')
        self.sourceList = QListWidget()
        rightContent = QVBoxLayout()
        rightContent.addWidget(rightLabel)
        rightContent.addWidget(self.sourceList)
        # Combine left and right content
        contentBox = QHBoxLayout()
        contentBox.addLayout(leftContent)
        contentBox.addLayout(rightContent)

        # Create button box
        self.buttonBox = QHBoxLayout()
        delButton = QPushButton('Delete')
        delButton.clicked.connect(self.deleteOrigin)
        self.buttonBox.addWidget(delButton)
        self.newOriginBtn = QPushButton('New Origin')
        self.newOriginBtn.clicked.connect(self.newOriginClicked)
        self.buttonBox.addWidget(self.newOriginBtn)

        # Combine content and button box
        self.layout = QVBoxLayout()
        self.layout.addLayout(contentBox)
        self.layout.addLayout(self.buttonBox)
        self.configLayout()
        self.setLayout(self.layout)
        self.fetchOrigin()
        self.originList.itemClicked.connect(self.originClicked)

        self.resetLists()

    def fetchOrigin(self):
        self.origins = self.originIo.getAll()
        for origin in self.origins:
            self.originList.addItem(origin.toString())

    def configLayout(self):
        self.setMinimumSize(640, 480)

    def originClicked(self, item):
        if len(self.origins) != 0:
            self.sourceList.clear()
            index = self.originList.selectedIndexes()[0].row()
            sources = self.sourceIo.getByOrigin(self.origins[index].id)
            for source in sources:
                self.sourceList.addItem(source.toString())

    def newOriginClicked(self):
        nOD = NewOriginDialog()
        nOD.exec_()
        self.resetLists()

    def deleteOrigin(self):
        id = self.origins[self.originList.selectedIndexes()[0].row()].id
        self.originIo.deleteById(id)
        self.sourceIo.deleteByOrigin(id)
        self.resetLists()

    def resetLists(self):
        self.originList.clear()
        self.sourceList.clear()
        self.fetchOrigin()
        self.originList.setCurrentRow(0)
        self.originClicked(0)
