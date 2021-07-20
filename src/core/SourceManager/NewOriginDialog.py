from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QComboBox, QLabel, QFileDialog, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon
from src.core.SourceManager.OriginTypes import OriginTypes

class NewOriginDialog(QDialog):
    def __init__(self):
        super(NewOriginDialog, self).__init__()

        # self.nextId = OriginIO().getHighestID()+1
        # self.originIO = OriginIO()
        # self.id = self.originIO.getNextId()
        # self.origin = Origin(id=self.id)
        #
        # # Layout
        # self.layout = QVBoxLayout()
        #
        # # Name
        # nameLayout = QHBoxLayout()
        # label = QLabel('Name')
        # nameLayout.addWidget(label)
        # self.nameTextEdit = QLineEdit()
        # nameLayout.addWidget(self.nameTextEdit)
        # self.layout.addLayout(nameLayout)
        #
        # # Type selection
        # typeSelectionLayout = QHBoxLayout()
        # typeLabel = QLabel('Type')
        # self.typeComboBox = QComboBox()
        # for t in OriginTypes:
        #     self.typeComboBox.addItem(t.name)
        # typeSelectionLayout.addWidget(typeLabel)
        # typeSelectionLayout.addWidget(self.typeComboBox)
        # self.layout.addLayout(typeSelectionLayout)
        # self.configLayout = QVBoxLayout()
        # self.typeComboBox.currentIndexChanged.connect(self.setConfigLayout)
        # self.typeComboBox.setCurrentIndex(0)
        #
        # # Script selector
        # # TODO: Dynamic layout by type
        # self.layout.addLayout(self.getPythonLayout())
        # self.setLayout(self.layout)

    def openScriptSelector(self, lable):
        file = QFileDialog.getOpenFileName(self, 'Select script', '.', 'Python file (*.py)')
        fileName = file[0].split('/')[-1]
        lable.setText(fileName)
        self.origin.script = fileName.split('.')[0]


    def setConfigLayout(self, index):
        if index is OriginTypes.PYTHON:
            self.configLayout.addLayout(self.getPythonLayout())

    def getPythonLayout(self):
        layout = QVBoxLayout()

        scriptSelectorLayout = QHBoxLayout()
        label = QLabel('Script')
        scriptSelectorLayout.addWidget(label)
        fileNameLabel = QLabel('')
        scriptSelectorLayout.addWidget(fileNameLabel)
        scriptSelectorBtn = QPushButton()
        scriptSelectorBtn.setIcon(QIcon('assets/icons/folder.png'))
        scriptSelectorLayout.addWidget(scriptSelectorBtn)
        scriptSelectorBtn.clicked.connect(lambda f: self.openScriptSelector(fileNameLabel))
        layout.addLayout(scriptSelectorLayout)

        # Ok, Cancle Button
        okBtn = QPushButton('')
        okBtn.setIcon(QIcon('assets/icons/done.png'))
        okBtn.clicked.connect(self.okBtnClicked)
        layout.addWidget(okBtn)

        # TODO: Register Source names
        return layout

    def okBtnClicked(self):
        self.origin.title = self.nameTextEdit.text()
        self.originIO.insert(self.origin)
        # TODO read source names and number from script and write to db
        self.accept()