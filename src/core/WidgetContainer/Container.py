from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtCore import Qt, QTimer
from src.DataManagement.IO.DataIO import DataIO
from src.DataManagement.IO.SourceIO import SourceIO
from src.core.SourceManager.SourceSelectionDialog import SourceSelectionDialog

class Container(QDockWidget):
    def __init__(self, widget, updateInterval=50):
        super(Container, self).__init__()

        self.sourceIO = SourceIO()
        self.dataIO = DataIO()
        self.timer = QTimer()
        self.widget = widget
        requiredSources = self.widget.requiredSources
        self.numberOfSources = len(requiredSources)
        sSD = SourceSelectionDialog(widget.requiredSources)

        # Get sources for data
        sSD.exec_()
        self.sources = sSD.sources

        # Load widget and start
        self.setWidget(widget)
        self.setFloating(True)
        self.updateInterval = updateInterval
        self.start()

    def start(self):
        self.updateInterval = self.updateInterval
        self.timer.setInterval(self.updateInterval)
        self.timer.timeout.connect(self.updateWidget)
        self.timer.start()

    def updateWidget(self):
        self.widget.update(*(self.dataIO.getLatestByIdAndOrigin(s.id, s.origin) for s in self.sources))
