from src.data_management.database.Connection import Connection
from src.data_management.database.io.IOErrors import SqlInsertError, SqlSelectError, SqlDeleteError
from src.data_management.dto.Data import Data


class DataIO:
    def __init__(self):
        self.db = Connection('data')

    def write(self, data: Data) -> None:
        cur = self.db.cursor()
        query = 'INSERT INTO data(source_id, set_id, "timestamp", "value") VALUES(?, ?, ?, ?)'
        try:
            cur.execute(query, data.__repr__())
            self.db.connection.commit()
        except Exception:
            raise SqlInsertError(data, 'data')

    def get_all_by_source_after(self, source_id: int, timestamp_ms: int) -> list:
        """ Return all values for source after a given timestamp """
        cur = self.db.cursor()
        query = 'SELECT * FROM "data" WHERE source_id = ? AND "timestamp" > ? ORDER BY timestamp DESC'
        try:
            cur.execute(query, (source_id, timestamp_ms))
            result = cur.fetchall()
            return result
        except Exception:
            raise SqlSelectError('data', 'get_all_by_source_after', f'{source_id=}, {timestamp_ms=}')

    def delete_all(self, source: int):
        cur = self.db.cursor()
        query = 'DELETE FROM "data" WHERE "source_id" = ?'
        try:
            cur.execute(query, (source,))
            self.db.commit()
        except Exception:
            raise SqlDeleteError('data', 'delete_all')