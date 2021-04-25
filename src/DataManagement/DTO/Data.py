from time import time_ns


class Data:
    def __init__(self, set=None, source=None, origin=None, data=None, timestamp=time_ns()):
        self.set = set
        self.source = source
        self.origin = origin
        self.data = data
        self.timestamp = timestamp

    def toTupel(self):
        return self.set, self.source, self.origin, self.data, self.timestamp
