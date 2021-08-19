from typing import List

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

    def get_all_by_source(self, source: int) -> List[Key]:
        cur = self.db.cursor()
        query = 'SELECT * FROM key WHERE source = ?'
        cur.execute(query, (source,))
        result = cur.fetchall()
        return [Key(*key) for key in result]

    def get_all(self):
        cur = self.db.cursor()
        query = 'SELECT * FROM key'
        cur.execute(query)
        result = cur.fetchall()
        return [Key(*key) for key in result]