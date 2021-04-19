from src.DataManagement.Database.Connection import Connection


class Source:
    def __init__(self, id=None, title=None, code=None):
        self.id = id
        self.code = code
        self.title = title

    def toTupel(self):
        return self.id, self.title, self.code

    def toString(self):
        return f'{self.id}: {self.title}'