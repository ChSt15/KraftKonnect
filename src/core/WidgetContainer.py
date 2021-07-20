from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtCore import Qt, QTimer
from src.DataManagement.IO.DataIO import DataIO
from src.DataManagement.IO.SourceIO import SourceIO
from src.DataManagement.IO.SetIO import SetIO
from src.core.SourceManager.SourceSelectionDialog import SourceSelectionDialog
from PyQt5.QtWidgets import QWidget


class Container(QDockWidget):
    def __init__(self, widget: QWidget, latest_record_id: int, update_interval: int = 100):
        super(Container, self).__init__()

        # IO objects
        self.sourceIO = SourceIO()
        self.dataIO = DataIO()
        self.timer = QTimer()
        self.widget = widget

        # ID of latest record
        self.latest_record_id = latest_record_id
        required_sources = self.widget.requiredSources
        self.numberOfSources = len(required_sources)

        # Choose data-sources
        source_selection_dialog = SourceSelectionDialog(widget.requiredSources)

        # Get sources for data
        source_selection_dialog.exec_()
        self.sources = source_selection_dialog.selected_sources

        # Load widget and start
        self.setWidget(widget)
        self.setFloating(True)
        self.update_interval = update_interval
        self.start()

    # Start widget updates
    def start(self):
        self.update_interval = self.updateInterval
        self.timer.setInterval(self.updateInterval)
        self.timer.timeout.connect(self.updateWidget)
        self.timer.start()

    # Update widget with all new data
    def update_widget(self):
        data = [self.dataIO.getBySourceAfter(source, self.)]
        data = [self.dataIO.getDataBySourceAndSet(source, self.currentSetId) for source in self.sources]
        dataAndTimestamps = [(dat.data, dat.timestamp) for dat in data]
        self.widget.update(dataAndTimestamps)

    # Set new set id
    def increment_set_id(self):
        self.latest_record_id = self.latest_record_id + 1

    def stop(self):
        self.timer.stop()
