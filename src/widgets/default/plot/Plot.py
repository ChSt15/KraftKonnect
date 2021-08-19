import time

from PyQt5.QtCore import QTimer
import pyqtgraph
from random import random
from typing import Tuple, List


class Plot(pyqtgraph.PlotWidget):

    required_keys = ['y-Axis']
    number_of_keys = len(required_keys)
    def __init__(self):
        super(Plot, self).__init__()
        # TODO Disable context menu and zoom/pan/etc
        pyqtgraph.setConfigOptions(antialias=True)
        self.maxHistory = 30
        # TODO Use AxisItem for time conversion and display
        self.x = []
        self.y = []
        self.start = int(time.time_ns() / 1000.0 / 1000.0)
        self.plot(x=self.x, y=self.y, clear=True)

    # Adds Data-points to plot. data must contain tuples with timestamp (x) and value (y).
    def update_data(self, data):
        for i, source in enumerate(data):
            # i is current source from required_sources
            if len(source) > 0:
                for d in source:
                    self.x.append((d[3]-self.start)/1000.0)
                    self.y.append(float(d[4]))
                    if len(self.x) > self.maxHistory:
                        self.x = self.x[1:]
                        self.y = self.y[1:]
        self.plot(self.x, self.y, clear=True)

