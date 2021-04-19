from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import random
from matplotlib.figure import Figure


class BasicPlot(FigureCanvas):

    def __init__(self, parent=None):
        fig, ax = plt.subplots()
        ax.plot([i for i in range(10)])
        super(BasicPlot, self).__init__(fig)
        self.setParent(parent)
