from src.DataManagement.Database.Connection import Connection
from src.DataManagement.DTO.Source import Source

class SourceIO:
    def __init__(self):
        self.db = Connection('source')

    def getByOrigin(self, origin):
        cur = self.db.cursor()
        query = 'SELECT * FROM source WHERE origin = ?'
        cur.execute(query, (origin,))
        rows = cur.fetchall()
        return [Source(*row) for row in rows]

    def getByOriginAndId(self, origin, id):
        cur = self.db.cursor()
        query = 'SELECT * FROM source WHERE origin = ? and id = ?'
        cur.execute(query, (origin, id))
        rows = cur.fetchall()
        return [Source(*row) for row in rows]

    def getAll(self):
        return self.db.getAll(Source)

    def deleteByOrigin(self, id):
        cur = self.db.cursor()
        query = 'DELETE FROM source WHERE origin = ?'
        cur.execute(query, (id,))
        self.db.connection.commit()