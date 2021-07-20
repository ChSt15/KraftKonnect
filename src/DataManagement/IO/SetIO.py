from src.DataManagement.Database.Connection import Connection
from src.DataManagement.DTO.Set import Set
from IOErrors import SqlInsertError

class SetIO:
    def __init__(self):
        self.db = Connection('set')

    def write(self, set):
        """ Insert a set into set table"""
        cur = self.db.cursor()
        query = 'INSERT INTO "set"(start_time_ms, end_time_ms) VALUES(?, ?)'
        cur.execute(query, set.__repr__())
        try:
            self.db.connection.commit()
        except Exception:
            raise SqlInsertError(set, 'set')

    def get_next_set_id(self):
        cur = self.db.cursor()
        query = 'SELECT set_id FROM sets ORDER BY set_id DESC LIMIT 1'
        cur.execute(query)
        res = cur.fetchone()
        return res[0]+1
