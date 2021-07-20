import time

from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtCore import Qt, QTimer
from src.DataManagement.IO.DataIO import DataIO
from src.DataManagement.IO.SourceIO import SourceIO
from src.DataManagement.IO.SetIO import SetIO
from src.core.SourceManager.SourceSelectionDialog import SourceSelectionDialog
from PyQt5.QtWidgets import QWidget


class Container(QDockWidget):
    # TODO: Replay function -> Use set_id and get historic data
    def __init__(self, widget: QWidget, update_interval: int = 100, set_id = None):
        super(Container, self).__init__()

        # IO objects
        self.source_io = SourceIO()
        self.data_io = DataIO()
        self.set_io = SetIO()

        self.last_update = None
        self.timer = QTimer()
        self.widget = widget
        self.next_set_id = self.set_io.get_next_set_id()
        self.required_sources = self.widget.requiredSources

        # Choose data-sources
        source_selection_dialog = SourceSelectionDialog(widget.requiredSources)

        # Get sources for data
        source_selection_dialog.exec_()
        self.sources_and_keys = source_selection_dialog.selected_sources_and_keys

        # Load widget and start
        self.setWidget(widget)
        self.setFloating(True)
        self.update_interval = update_interval
        self.start()

    # Start widget updates
    def start(self):
        self.last_update = int(time.time_ns()/1000)
        self.timer.setInterval(self.update_interval)
        self.timer.timeout.connect(self.update_widget)
        self.timer.start()

    # Update widget with all new data
    def update_widget(self):
        """ Get latest data from database by source and key and send to widget"""
        data = [[self.dataIO.get_all_by_source_and_key_after(s.id, s.key, self.last_update)] for s in self.sources_and_keys]
        self.last_update = int(time.time_ns()/1000)
        self.widget.update(data)

    # Set new set id
    def increment_set_id(self):
        self.next_set_id = self.latest_record_id + 1

    def stop(self):
        self.timer.stop()
        self.increment_set_id()
