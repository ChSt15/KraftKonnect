from PyQt5.QtWidgets import QWidget, QMdiSubWindow, QLabel, QSpacerItem, QToolButton, QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt5 import uic
from PyQt5.QtCore import Qt

class Container(QMdiSubWindow):
    def __init__(self, widget=None, label="Container"):
        super(Container, self).__init__()
        self.setWidget(widget)
        self.setWindowTitle(label)
        #self.setWindowFlag(Qt.FramelessWindowHint)

