from src.DataManagement.Database.Connection import Connection
from src.DataManagement.DTO.Set import Set

class SetIO:
    def __init__(self):
        self.db = Connection('set')

    def getNextSetId(self):
        cur = self.db.cursor()
        query = 'SELECT id FROM sets ORDER BY id DESC LIMIT 1'
        cur.execute(query)
        res = cur.fetchone()
        return res[0]+1

    def write(self, set):
        cur = self.db.cursor()
        query = 'INSERT INTO sets VALUES(?, ?, ?)'
        cur.execute(query, set.toTupel())
        self.db.connection.commit()

    def get_next_set_id(self):
        cur = self.db.cursor()
        query = 'SELECT set_id FROM sets ORDER BY set_id DESC LIMIT 1'
        cur.execute(query)
        res = cur.fetchone()
        return res[0]
