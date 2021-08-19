from src.data_management.database.Connection import Connection
from src.data_management.dto.Key import Key


class KeyIO:
    def __init__(self):
        self.db = Connection('set')

    def insert(self, key: Key):
        cur = self.db.cursor()
        query = 'INSERT INTO key(name, source) VALUES(?, ?)'
        cur.execute(query, (key.name, key.source))
        self.db.connection.commit()

    def get_by_id(self, id: int) -> Key:
        cur = self.db.cursor()
        query = 'SELECT * FROM key WHERE id = ?'
        cur.execute(query, (id,))
        result = cur.fetchone()
        return Key(*result)