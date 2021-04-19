class Data:
    def __init__(self, source=None, sensor=None, data=None, time=None):
        self.source = source
        self.sensor = sensor
        self.data = data
        self.time = time

    def toTupel(self):
        return self.source, self.sensor, self.data, self.time
