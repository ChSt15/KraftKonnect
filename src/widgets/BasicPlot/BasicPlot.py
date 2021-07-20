from PyQt5.QtCore import QTimer
from pyqtgraph import PlotWidget
from random import random
from typing import Tuple, List


class BasicPlot(PlotWidget):

    requiredSources = ['x-Axis']
    numberOfSources = len(requiredSources)
    xi = 0
    def __init__(self):
        super(BasicPlot, self).__init__()
        self.maxHistory = 30
        self.x = []
        self.y = []
        self.plot(x=self.x, y=self.y, clear=True)

    # Adds Data-points to plot. data must contain tuples with timestamp (x) and value (y).
    def update(self, data):
        # for d in data:
        #     self.x.append(d[0])
        #     self.y.append(d[1])
        self.x.append(self.xi)
        self.xi += 1
        self.y.append(random())
        self.plot(self.x, self.y, clear=True)

