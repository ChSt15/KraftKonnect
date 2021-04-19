from PyQt5.QtCore import QTimer
from pyqtgraph import PlotWidget
from random import random


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

    def update(self, *data):
        yData = data[0]
        self.x = self.x[1:]
        self.x.append(self.x[-1]+1)
        self.y = self.y[1:]
        self.y.append(yData)
        self.plotRef.setData(self.x, self.y)
