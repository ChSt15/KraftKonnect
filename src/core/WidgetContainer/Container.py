from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtCore import Qt, QTimer
from src.DataManagement.IO.DataIO import DataIO
from src.DataManagement.IO.SourceIO import SourceIO
from src.DataManagement.IO.SetIO import SetIO
from src.core.SourceManager.SourceSelectionDialog import SourceSelectionDialog
from PyQt5.QtWidgets import QWidget

class Container(QDockWidget):
    def __init__(self, widget: QWidget, setId: int, updateInterval: float = 100):
        super(Container, self).__init__()

        self.sourceIO = SourceIO()
        self.dataIO = DataIO()
        self.timer = QTimer()
        self.widget = widget
        self.currentSetId = setId
        requiredSources = self.widget.requiredSources
        self.numberOfSources = len(requiredSources)
        sSD = SourceSelectionDialog(widget.requiredSources)

        # Get sources for data
        sSD.exec_()
        self.sources = sSD.selectedSources

        # Load widget and start
        self.setWidget(widget)
        self.setFloating(True)
        self.updateInterval = updateInterval
        self.start()

    # Start continous widget updates
    def start(self):
        self.updateInterval = self.updateInterval
        self.timer.setInterval(self.updateInterval)
        self.timer.timeout.connect(self.updateWidget)
        self.timer.start()

    # Update widget once
    def updateWidget(self):
        # TODO fetch only latest
        data = [self.dataIO.getDataBySourceAndSet(source, self.currentSetId) for source in self.sources]
        dataAndTimestamps = [(dat.data, dat.timestamp) for dat in data]
        self.widget.update(dataAndTimestamps)

    # Set new set id
    def setSetId(self, id):
        self.currentSetId = id

    def stop(self):
        self.timer.stop()