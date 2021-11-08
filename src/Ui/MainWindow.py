import time

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QAction
from PyQt5.QtCore import Qt

from src.Ui.SourceAddDialog import SourceAddDialog
from src.Ui.KeySelectionDialog import KeySelectionDialog
from src.data_management.SourceLoader import Collector
from src.data_management.database.io.SetIO import SetIO
from src.data_management.database.Key import Key
from src.data_management.database.Source import Source
from src.widgets.WidgetContainer import Container
from src.Ui.SourceManagerDialog import SourceManagerDialog
from src.data_management.database.Set import Set
from src.data_management.database.io.KeyInSetIO import KeyInSetIO
import pkgutil
import src.widgets.default as widgets
import importlib


class CoreWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.containers = []
        self.sources = []
        self.keys = []
        self.collectors = []
        self.set_start_time = None
        self.set_up_ui()

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
        self.action_start.triggered.connect(self.set_start)
        self.action_stop.triggered.connect(self.set_stop)
        self.action_stop.setEnabled(False)
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
        keys = []
        widget = cls()
        required_keys = widget.required_keys
        if len(required_keys) != 0:
            key_selection_dialog = KeySelectionDialog(required_keys)
            key_selection_dialog.exec_()
            # map(self.register_source, sources)
            keys = key_selection_dialog.selected_keys
            map(self.register_key, keys)
            # TODO Check if btn was cancel/ok instead of source quality
        if all(map(lambda x: x != "None" and x is not None, keys)):
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

    def set_stop(self):
        key_in_set_io = KeyInSetIO()
        set_io = SetIO()
        set_stop_time = time.time_ns()
        set_id = set_io.get_next_set_id()
        set_io.write(Set(set_id, self.set_start_time, set_stop_time))
        for key in self.keys:
            key_in_set_io.insert(key, set_id)
        self.menu_set.action_start.setEnabled(True)
        self.menu_set.action_stop.setEnabled(False)

    def set_start(self):
        self.set_start_time = time.time_ns()
        self.menu_set.action_start.setEnabled(False)
        self.menu_set.action_stop.setEnabled(True)

