from PyQt5.QtCore import QTimer
from pyqtgraph import PlotWidget
from random import random
from typing import Tuple, List


class BasicPlot(PlotWidget):

    requiredSources = ['x-Axis']
    numberOfSources = len(requiredSources)

    def __init__(self):
        super(BasicPlot, self).__init__()
        self.maxHistory = 30
        # TODO: Fix no initial graph shown
        self.x = [0 for i in range(self.maxHistory)]
        self.y = [0 for i in range(self.maxHistory)]
        self.plotRef = self.plot(self.x, self.y)
        self.setAntialiasing(True)

    # Redraw plot. data is a list with tuples for each source and each contains data and timestamp
    def update(self, data):
        self.x = self.x[1:]
        # TODO: Real time
        self.x.append(self.x[-1]+1)
        self.y = self.y[1:]
        self.y.append(data[0][0])
        self.plotRef.setData(self.x, self.y)
