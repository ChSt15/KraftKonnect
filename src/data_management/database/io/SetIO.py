from src.DataManagement.Database.Connection import Connection
from src.DataManagement.DTO.Set import Set
from src.DataManagement.IO.IOErrors import SqlInsertError, SqlSelectError

class SetIO:
    def __init__(self):
        self.db = Connection('set')

    def write(self, set):
        """ Insert a set into set table"""
        cur = self.db.cursor()
        query = 'INSERT INTO "set"(start_time_ms, end_time_ms) VALUES(?, ?)'
        try:
            cur.execute(query, set.__repr__())
            self.db.connection.commit()
        except Exception:
            raise SqlInsertError(set, 'set')

    def get_next_set_id(self):
        cur = self.db.cursor()
        query = 'SELECT "id" FROM "set" ORDER BY "id" DESC LIMIT 1'
        try:
            cur.execute(query)
            res = cur.fetchone()
            return res[0]+1
        except:
            raise SqlSelectError('set', 'get_next_set_id')
