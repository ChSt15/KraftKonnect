from src.data_management.database.Connection import Connection
from src.data_management.database.io.IOErrors import SqlInsertError, SqlSelectError, SqlDeleteError
from src.data_management.dto.Data import Data


class DataIO:
    def __init__(self):
        self.db = Connection('data')

    def insert(self, data: Data) -> None:
        cur = self.db.cursor()
        query = 'INSERT INTO data(key, "time", "value") VALUES(?, ?, ?, ?)'
        cur.execute(query, (data.key, data.time, data.value))
        self.db.connection.commit()


    def get_all_by_key_after(self, key: int, time: int) -> list:
        """ Return all values for source after a given timestamp """
        cur = self.db.cursor()
        query = 'SELECT * FROM "data" WHERE key = ? AND "time" > ? ORDER BY time DESC'
        try:
            cur.execute(query, (key, time))
            result = cur.fetchall()
            return result
        except Exception:
            raise SqlSelectError('data', 'get_all_by_source_after', f'{key=}, {time=}')

    def delete_all_by_key(self, key: int):
        cur = self.db.cursor()
        query = 'DELETE FROM "data" WHERE "key" = ?'
        try:
            cur.execute(query, (key,))
            self.db.commit()
        except Exception:
            raise SqlDeleteError('data', 'delete_all')