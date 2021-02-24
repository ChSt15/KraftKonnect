from PyQt6 import QtGui, QtWidgets, uic


class CoreWindow(QtWidgets.QMainWindow):

    def __init__(self, conf_path=None):
        super(CoreWindow, self).__init__()
        if conf_path is None:
            uic.loadUi("src/core/coreWindow.ui", self)
        else:
            # Generate window view from xml/yaml file
            # E.g. create specified widgets and fetch all data
            pass
        self.showMaximized()