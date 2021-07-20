from PyQt5.QtWidgets import QMainWindow, QAction, QWidget
from PyQt5.QtCore import Qt
from src.widgets.BasicPlot.BasicPlot import BasicPlot
from src.core.WidgetContainer import Container
from src.core.SourceManager.SourceManagerDialog import SourceManagerDialog
from src.DataManagement.IO.OriginIO import OriginIO
from src.DataManagement.IO.SetIO import SetIO
from src.DataManagement.DataCollector.Collector import Collector
from time import time_ns
from src.DataManagement.DTO.Set import Set

class CoreWindow(QMainWindow):



    def __init__(self):
        super().__init__()

        self.menu = self.menuBar()
        self.setUpMenuBar()
        self.configureLayout()
        self.originIO = OriginIO()
        self.setIO = SetIO()
        self.currentSet = self.setIO.getLatest()
        self.collectors = []
        self.containers = []


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

        runMenu = self.menu.addMenu('Run')
        runStartAction = QAction('Start', self)
        runStopAction = QAction('Stop', self)
        runStartAction.triggered.connect(self.setStart)
        runStopAction.triggered.connect(self.setStop)
        runMenu.addAction(runStartAction)
        runMenu.addAction(runStopAction)

    # Open manager to delete, rename, config origins and sources
    def launchSourceManager(self):
        sm = SourceManagerDialog()
        sm.exec_()

    # Layout specific configs
    def configureLayout(self) -> None:
        self.setDockNestingEnabled(True)
        self.showMaximized()

    # Add new single-x-axis plot from menu bar
    def newBasicPlotWidget(self) -> None:
        basicBlot = BasicPlot()
        self.attachWidget(basicBlot)

    # Add widget to screen
    def attachWidget(self, widget: QWidget) -> None:
        container = Container(widget, self.currentSet.id)
        self.containers.append(container)
        self.addDockWidget(Qt.BottomDockWidgetArea, container)

    # Start data recording, logging, displaying
    def setStart(self) -> None:
        setId = self.setIO.getNextSetId()
        self.setGlobalContainerId(setId)
        self.startContainerUpdates()
        origins = self.originIO.getAll()
        set = Set(id=setId)
        set.id = self.currentSet.id + 1
        set.start = time_ns()
        self.currentSet = set
        for origin in origins:
            collector = Collector(origin)
            self.collectors.append(collector)
            collector.start()

    # Stop data recording, logging, displaying
    def setStop(self) -> None:
        while len(self.collectors) > 0:
            collector = self.collectors.pop()
            collector.stop()
        self.currentSet.end = time_ns()
        self.setIO.write(self.currentSet)
        self.stopContainerUpdates()

    def setGlobalContainerId(self, id):
        for container in self.containers:
            container.currentSetId = id

    def stopContainerUpdates(self):
        for container in self.containers:
            container.stop()

    def startContainerUpdates(self):
        for container in self.containers:
            container.start()