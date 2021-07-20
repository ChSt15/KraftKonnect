from src.DataManagement.Database.Connection import Connection
from src.DataManagement.DTO.Data import Data
from src.DataManagement.DTO.Source import Source


class DataIO:
    def __init__(self):
        self.db = Connection('data')

    def write(self, data):
        cur = self.db.cursor()
        query = 'INSERT INTO data VALUES(?, ?, ?, ?)'
        cur.execute(query, data.__repr__())
        self.db.connection.commit()

    def get_all_by_source_after(self, source_id, timestamp_ms):
        """ Return all values for source after a given timestamp """
        cur = self.db.cursor()
        query = 'SELECT * FROM data WHERE source_id = ? AND timestamp > ? ORDER BY timestamp DESC'
        cur.execute(query, (source_id, timestamp_ms))
        result = cur.fetchall()
        return result
