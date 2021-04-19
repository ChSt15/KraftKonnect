class Source:
    def __init__(self, id, origin, name):
        self.id = id
        self.origin = origin
        self.name = name

    def toTupel(self):
        return self.id, self.name

    def toString(self):
        return f'{self.id}: {self.name}'

    def toOriginNameRepr(self):
        return f'Origin {self.origin}: {self.name}'