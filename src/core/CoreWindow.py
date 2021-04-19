from PyQt5.QtWidgets import QMainWindow, QAction, QDockWidget
from PyQt5.QtCore import Qt
from PyQt5 import uic
from src.widgets.BasicPlot.BasicPlot import BasicPlot
from src.core.WidgetContainer.Container import Container
from src.core.SourceManager.SourceManagerDialog import SourceManagerDialog
from src.core.SourceManager.SourceSelectionDialog import SourceSelectionDialog

class CoreWindow(QMainWindow):



    def __init__(self):
        super().__init__()

        self.menu = self.menuBar()
        self.setUpMenuBar()
        self.configureLayout()


    def setUpMenuBar(self):
        widgetMenu = self.menu.addMenu('Widgets')
        addWidgetMenu = widgetMenu.addMenu('Add')
        basicPlotWidgetAction = QAction('Basic Plot', self)
        addWidgetMenu.addAction(basicPlotWidgetAction)
        basicPlotWidgetAction.triggered.connect(self.newBasicPlotWidget)


        sourceMenu = self.menu.addMenu('Data')
        actionManager = QAction('Manager', self)
        actionManager.triggered.connect(self.launchSourceManager)
        sourceMenu.addAction(actionManager)

    def launchSourceManager(self):
        sm = SourceManagerDialog()
        sm.exec_()

    def configureLayout(self):
        self.setDockNestingEnabled(True)
        self.showMaximized()

    def newBasicPlotWidget(self):
        basicBlot = BasicPlot()
        self.attachWidget(basicBlot)

    def attachWidget(self, widget):
        self.addDockWidget(Qt.BottomDockWidgetArea, Container(widget))