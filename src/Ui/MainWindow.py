import time

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QWidget, QAction
from PyQt5.QtCore import Qt

from src.Ui.SourceAddDialog import SourceAddDialog
from src.Ui.SourceSelectionDialog import SourceSelectionDialog
from src.data_management.Collector import Collector
from src.data_management.database.io.SetIO import SetIO
from src.data_management.dto.Key import Key
from src.data_management.dto.Source import Source
from src.widgets.WidgetContainer import Container
from src.Ui.SourceManagerDialog import SourceManagerDialog
from src.data_management.dto.Set import Set
from src.data_management.database.io.KeyInSetIO import KeyInSetIO
import pkgutil
import src.widgets.default as widgets
import importlib


class CoreWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.set_up_ui()
        self.containers = []
        self.sources = []
        self.keys = []
        self.collectors = []
        self.set_start_time = None
        self.set_io = SetIO()

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
        self.menu_set.action_start.triggered.connect(self.set_start)
        self.menu_set.action_stop.triggered.connect(self.stop_set())
        self.menu_set.action_stop.setEnabled(False)
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
        sources = []
        keys = []
        if widget.required_sources is not None:
            source_selection_dialog = SourceSelectionDialog(widget.required_sources)
            source_selection_dialog.exec_()
            sources = source_selection_dialog.selected_sources
            map(self.register_source, sources)
            keys = source_selection_dialog.keys
            map(self.register_key, keys)
            # TODO Check if btn was cancel/ok instead of source quality
        if all(map(lambda x: x != "None" and x is not None, sources)):
            container = Container(cls(), keys)
            self.containers.append(container)
            self.addDockWidget(Qt.BottomDockWidgetArea, container)

    def register_source(self, source: Source):
        if source not in self.sources:
            self.collectors.append(Collector(source))
            self.sources.append(source)

    def register_key(self, key: Key):
        if key not in self.keys:
            self.keys.append(key)

    def stop_set(self):
        key_in_set_io = KeyInSetIO()
        set_stop_time = time.time_ns()
        set_id = self.set_io.get_next_set_id()
        self.set_io.write(Set(set_id, self.set_start_time, set_stop_time))
        for key in self.keys:
            key_in_set_io.insert(key, set_id)
        self.menu_set.action_start.setEnabled(True)
        self.menu_set.action_stop.setEnabled(False)

    def start_set(self):
        self.set_start_time = time.time_ns()
        self.menu_set.action_start.setEnabled(False)
        self.menu_set.action_stop.setEnabled(True)

