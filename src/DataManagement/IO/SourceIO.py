from src.DataManagement.Database.Connection import Connection
from src.DataManagement.DTO.Source import Source
from src.DataManagement.IO.IOErrors import SqlInsertError, SqlSelectError


class SourceIO:
    def __init__(self):
        self.db = Connection('source')

    def get_all(self):
        cur = self.db.cursor()
        query = 'SELECT * FROM source'
        cur.execute(query)
        try:
            rows = cur.fetchall()
            return [Source(*row) for row in rows]
        except Exception:
            raise SqlSelectError('source', 'get_all')