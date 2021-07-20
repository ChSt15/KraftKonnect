from src.DataManagement.Database.Connection import Connection
from src.DataManagement.DTO.Data import Data
from src.DataManagement.DTO.Source import Source
from IOErrors import SqlInsertError, SqlSelectError


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
