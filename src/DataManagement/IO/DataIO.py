from src.DataManagement.Database.Connection import Connection

class DataIO:
    def __init__(self):
        self.db = Connection('data')

    def write(self, data):
        self.db.write(data.toTuple())

