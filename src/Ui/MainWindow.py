from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QWidget, QAction
from PyQt5.QtCore import Qt

from src.Ui.SourceAddDialog import SourceAddDialog
from src.Ui.SourceSelectionDialog import SourceSelectionDialog
from src.widgets.WidgetContainer import Container
from src.Ui.SourceManagerDialog import SourceManagerDialog
import pkgutil
import src.widgets.default as widgets
import importlib


class CoreWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.set_up_ui()
        self.sources = []
        self.containers = []

    # Open manager to delete, rename, config origins and sources
    @staticmethod
    def launch_source_manager_dialog():
        sm = SourceManagerDialog()
        sm.exec_()

    # Load ui stuff and configure buttons etc
    def set_up_ui(self) -> None:
        uic.loadUi('res/layout/main_window.ui', self)
        self.showMaximized()
        self.actionManager.triggered.connect(self.launch_source_manager_dialog)
        self.add_source.triggered.connect(self.launch_source_add_dialog)
        # Load all default widgets to menu
        for module_finder, name, ispkg in pkgutil.iter_modules(widgets.__path__):
            module = importlib.import_module(f'.{name}.{name[0].upper()+name[1:]}', 'src.widgets.default')
            name = name[0].upper()+name[1:]
            action = QAction(name, self)
            cls = getattr(module, name)
            action.triggered.connect(lambda ac, cls=cls: self.attach_widget(cls))
            self.menu_widgets.addAction(action)

    def launch_source_add_dialog(self):
        sad = SourceAddDialog()
        sad.exec_()

    # Add widget to screen
    def attach_widget(self, cls) -> None:
        widget = cls()
        source_selection_dialog = SourceSelectionDialog(widget.required_sources)
        source_selection_dialog.exec_()
        sources = source_selection_dialog.selected_sources
        # TODO Check if btn was cancel/ok instead of source quality
        # Check if all sources set, else do noting
        if all(map(lambda x: x != "None" and x is not None, sources)):
            container = Container(cls(), sources)
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
