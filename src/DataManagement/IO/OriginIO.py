from src.DataManagement.Database.Connection import Connection
from src.DataManagement.DTO import Source
from src.DataManagement.DTO.Origin import Origin

class OriginIO:
    def __init__(self):
        self.db = Connection('origin')

    def getCode(self, id):
        cur = self.db.cursor()
        cur.execute('SELECT code FROM source WHERE id=?', id)
        # TODO return code

    def getAll(self):
        cur = self.db.cursor()
        cur.execute('SELECT * FROM origin')
        rows = cur.fetchall()
        if rows is None:
            print('[LOG] Queried 0 sources.')
            return None
        try:
            return [Origin(*row) for row in rows]
        except:
            Exception('[ERROR] Error while fetching sources.')

    def getHighestID(self):
        cur = self.db.cursor()
        cur.execute('SELECT id FROM origin ORDER BY id DESC LIMIT 1')
        res = cur.fetchone()
        if res is None:
            return 0
        else:
            return res[0]
    
    def insert(self, origin: Origin):
        cur = self.db.cursor()
        query = 'INSERT INTO origin VALUES(?, ?, ?)'
        cur.execute(query, origin.toTupel())
        self.db.connection.commit()

    def getNextId(self):
        return self.getHighestID()+1

    def deleteById(self, id):
        cur = self.db.cursor()
        query = 'DELETE FROM origin WHERE id = ?'
        cur.execute(query, (id, ))
        self.db.connection.commit()