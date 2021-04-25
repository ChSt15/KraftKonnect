from src.DataManagement.Database.Connection import Connection


class Origin:
    def __init__(self, id=None, title=None, script=None):
        self.id = id
        self.script = script
        self.title = title

    def toTupel(self):
        return self.id, self.title, self.script

    def toString(self):
        return f'{self.id}: {self.title}'