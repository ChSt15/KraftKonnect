import time

from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtCore import QTimer
from src.DataManagement.IO.DataIO import DataIO
from src.DataManagement.IO.SourceIO import SourceIO
from src.DataManagement.IO.SetIO import SetIO
from src.core.SourceSelectionDialog import SourceSelectionDialog
from PyQt5.QtWidgets import QWidget


class Container(QDockWidget):
    # TODO: Replay function -> Use set_id and get historic data
    def __init__(self, widget: QWidget, update_interval: int = 30, set_id = None):
        super(Container, self).__init__()

        # IO objects
        self.source_io = SourceIO()
        self.data_io = DataIO()
        self.set_io = SetIO()

        self.last_update = None
        self.timer = QTimer()
        self.widget = widget
        self.next_set_id = self.set_io.get_next_set_id()
        self.required_sources = self.widget.required_sources

        # Choose data-sources
        source_selection_dialog = SourceSelectionDialog(widget.required_sources)

        # Get sources for data
        source_selection_dialog.exec_()
        self.sources = source_selection_dialog.selected_sources

        # Load widget and start
        self.setWidget(widget)
        #self.setFloating(True)
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
        """ Get latest data by source and send to widget"""
        data = [self.data_io.get_all_by_source_after(s.id, self.last_update) for s in self.sources]
        self.last_update = int(time.time_ns()/1000)
        self.widget.update_data(data)

    # Set new set id
    def increment_set_id(self):
        self.next_set_id = self.latest_record_id + 1

    def stop(self):
        self.timer.stop()
        self.increment_set_id()
