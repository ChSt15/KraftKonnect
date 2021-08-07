from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import Qt
from src.widgets.WidgetContainer import Container
from src.Ui.SourceManagerDialog import SourceManagerDialog
from src.widgets.default.rotation.Rotation import Rotation
from src.widgets.default.plot.Plot import BasicPlot


class CoreWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.set_up_ui()
        self.sources = []
        self.containers = []

    # Open manager to delete, rename, config origins and sources
    @staticmethod
    def launch_source_manager():
        sm = SourceManagerDialog()
        sm.exec_()

    # Layout specific configs
    def set_up_ui(self) -> None:
        uic.loadUi('res/layout/main_window.ui', self)
        self.showMaximized()
        a = self.actionManager.triggered.connect(self.launch_source_manager)

    # TODO autmoatically add all widgets from default widgets folder
    # def load_default_widgets(self):
    #     widget_menu = self.menu.addMenu('widgets')
    #     plot = QAction('Basic Plot', self)
    #     rotation = QAction('rotation', self)
    #     plot.triggered.connect(self.newBasicPlotWidget)
    #     plot.triggered.connect(self.newRotationWidget)
    #     widget_menu.addAction(plot)
    #     widget_menu.addAction(rotation)

    # # Add new single-x-axis plot from menu bar
    def newBasicPlotWidget(self) -> None:
        basicBlot = BasicPlot()
        self.attach_widget(basicBlot)

    def newRotationWidget(self) -> None:
        rotationWidget = Rotation()
        self.attach_widget(rotationWidget)

    # Add widget to screen
    def attach_widget(self, widget: QWidget) -> None:
        container = Container(widget)
        self.containers.append(container)
        self.addDockWidget(Qt.BottomDockWidgetArea, container)

    def stop_container_updates(self):
        """ Start every registered container """
        for container in self.containers:
            container.stop()

    def start_container_updates(self):
        """ Stop every registered container """
        for container in self.containers:
            container.start()
