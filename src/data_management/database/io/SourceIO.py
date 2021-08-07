import sqlite3
from sqlite3 import IntegrityError, Error, OperationalError

from src.data_management.database.Connection import Connection
from src.data_management.database.io.IOErrors import SqlSelectError, SqlDeleteError
from src.data_management.dto.Source import Source


class SourceIO:
    def __init__(self):
        self.db = Connection('source')

    def get_all(self):
        cur = self.db.cursor()
        query = 'SELECT * FROM source'
        try:
            cur.execute(query)
            rows = cur.fetchall()
            return [Source(*row) for row in rows]
        except Exception:
            raise SqlSelectError('source', 'get_all')

    def delete(self, id: int):
        cur = self.db.cursor()
        query = 'DELETE FROM "source" WHERE "id" = ?'
        try:
            cur.execute(query, (id,))
            self.db.commit()
        except Exception:
            raise SqlDeleteError('source', 'delete')

    def update(self, source):
        cur = self.db.cursor()
        query = 'UPDATE "source" SET name = ?, description = ?, "script" = ? WHERE "id" = ?'
        try:
            cur.execute(query, (source.name, source.description, source.script, source.id))
            self.db.commit()
        except IntegrityError:
            raise
