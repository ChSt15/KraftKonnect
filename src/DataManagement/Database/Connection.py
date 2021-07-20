import sqlite3

class Connection:
    def __init__(self, table):
        self.connection = sqlite3.connect('database.db')
        self.table = table

        # Test table exists
        # try:
        #     self.connection.cursor().execute('SELECT * FROM ?', (self.table, ))
        # except:
        #    raise Exception(f'[ERROR] Table {self.table} not found.')

    def insert(self, *data):
        cur = self.cursor()
        query = 'INSERT INTO ? VALUES(?)'
        cur.execute(query, (self.table, data))
        self.connection.commit()

    def cursor(self):
        return self.connection.cursor()

    def getAll(self, objectClass=None):
        cur = self.cursor()
        # TODO WHY DOESNT IT WORK???
        # query = 'SELECT * FROM ?'
        # cur.execute(query, ('source', ))
        cur.execute(f'SELECT * FROM {self.table}')
        rows = cur.fetchall()
        if objectClass is None:
            return rows
        else:
            return [objectClass(*row) for row in rows]