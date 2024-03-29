import sqlite3


class Connection:
    def __init__(self, table):
        self.connection = sqlite3.connect('database.db')
        self.table = table

    def commit(self):
        self.connection.commit()

    def cursor(self):
        return self.connection.cursor()
