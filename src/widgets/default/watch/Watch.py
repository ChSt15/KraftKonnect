import matplotlib
from PyQt5 import uic
from PyQt5.QtCore import QTime, QElapsedTimer
from PyQt5.QtWidgets import QWidget

matplotlib.use('Qt5Agg')


class Watch(QWidget):

    required_keys = []
    update_interval = 30

    def __init__(self):
        super().__init__()
        uic.loadUi('src/widgets/default/watch/watch.ui', self)
        self.timer = QElapsedTimer()
        self.timer.start()

    def update_data(self, data):
        pass

    def redraw(self):
        self.lcd.display(format(self.timer.elapsed() / 1000, '.3f'))
        self.progress.setValue(self.timer.elapsed() % 1000 / 10)