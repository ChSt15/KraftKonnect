import time

from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtCore import QTimer
from src.Ui.KeySelectionDialog import KeySelectionDialog
from PyQt5.QtWidgets import QWidget

from src.data_management.database.io.DataIO import DataIO
from src.data_management.database.io.SetIO import SetIO
from src.data_management.database.io.SourceIO import SourceIO


class Container(QDockWidget):
    # TODO: Replay function -> Use set_id and get historic data
    def __init__(self, widget: QWidget, keys):
        super(Container, self).__init__()

        # io objects
        self.source_io = SourceIO()
        self.data_io = DataIO()
        self.keys = keys
        self.last_update = int(time.time_ns()/1000.0/1000.0)
        self.timer = QTimer()
        self.widget = widget

        # Load widget and start
        self.setWidget(widget)
        self.setFloating(True)
        self.start()

    # Start widget updates
    def start(self):
        self.timer.setInterval(max(30, self.widget.update_interval))
        self.timer.timeout.connect(self.update_widget)
        self.timer.start()

    # Update widget with all new data
    def update_widget(self):
        self.widget.update_data([[()]])
        self.widget.redraw()
        # data = [self.data_io.get_all_by_key_after(key.id, self.last_update) for key in self.keys]
        # self.widget.update_data(data)

    def stop(self):
        self.timer.stop()
