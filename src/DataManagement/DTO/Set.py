class Set:
    def __init__(self, id=None, start=None, end=None):
        self.id = id
        self.start = start
        self.end = end

    def toTupel(self):
        return self.id, self.start, self.end