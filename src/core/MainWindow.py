from PyQt5.QtWidgets import QMainWindow, QAction, QWidget
from PyQt5.QtCore import Qt
from src.widgets.BasicPlot.BasicPlot import BasicPlot
from src.widgets.WidgetContainer import Container
from src.core.SourceManager.SourceManagerDialog import SourceManagerDialog
from src.DataManagement.IO.SetIO import SetIO
from src.DataManagement.DataCollector.Collector import Collector
from time import time_ns
from src.DataManagement.DTO.Set import Set


class CoreWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.menu = self.menuBar()
        self.set_up_menu_bar()
        self.configure_layout()
        self.set_io = SetIO()
        self.current_set = None
        self.sources = []
        self.collectors = []
        self.containers = []

    def set_up_menu_bar(self):
        widget_menu = self.menu.addMenu('Widgets')
        add_widget_menu = widget_menu.addMenu('Add')
        # basic_plot_widget_action = QAction('Basic Plot', self)
        # add_widget_menu.addAction(basic_plot_widget_action)
        # basic_plot_widget_action.triggered.connect(self.newBasicPlotWidget)

        source_menu = self.menu.addMenu('Data')
        action_manager = QAction('Manager', self)
        action_manager.triggered.connect(self.launch_source_manager)
        source_menu.addAction(action_manager)

        run_menu = self.menu.addMenu('Run')
        run_start_action = QAction('Start', self)
        run_stop_action = QAction('Stop', self)
        run_start_action.triggered.connect(self.set_start_recording)
        run_stop_action.triggered.connect(self.set_stop_recording)
        run_menu.addAction(run_start_action)
        run_menu.addAction(run_stop_action)

    # Open manager to delete, rename, config origins and sources
    @staticmethod
    def launch_source_manager():
        sm = SourceManagerDialog()
        sm.exec_()

    # Layout specific configs
    def configure_layout(self) -> None:
        self.setDockNestingEnabled(True)
        self.showMaximized()

    # TODO autmoatically add all widgets in default widgets folder
    # # Add new single-x-axis plot from menu bar
    # def newBasicPlotWidget(self) -> None:
    #     basicBlot = BasicPlot()
    #     self.attachWidget(basicBlot)

    # Add widget to screen
    def attach_widget(self, widget: QWidget) -> None:
        container = Container(widget)
        self.containers.append(container)
        self.addDockWidget(Qt.BottomDockWidgetArea, container)

    # Start data recording, logging, displaying
    def set_start_recording(self) -> None:
        next_set_id = self.setIO.get_next_set_id()
        self.start_container_updates()
        self.current_set = Set(next_set_id, int(time_ns()/1000), None)
        for container in self.containers:
            for source, _ in container.sources_and_keys:
                if source not in self.sources:
                    self.sources.append(source)
        for source in self.sources:
            collector = Collector(source)
            self.collectors.append(collector)
            collector.start()

    def set_stop_recording(self) -> None:
        self.stopContainerUpdates()
        self.currentSet.end_time_ms = int(time_ns()/1000)
        while len(self.collectors) > 0:
            collector = self.collectors.pop()
            collector.stop()
        self.setIO.write(self.currentSet)

    def stop_container_updates(self):
        """ Start every registered container """
        for container in self.containers:
            container.stop()

    def start_container_updates(self):
        """ Stop every registered container """
        for container in self.containers:
            container.start()
