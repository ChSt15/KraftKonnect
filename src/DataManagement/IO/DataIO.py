from src.DataManagement.Database.Connection import Connection
from src.DataManagement.DTO.Data import Data
from src.DataManagement.DTO.Source import Source

class DataIO:
    def __init__(self):
        self.db = Connection('data')

    def getAllBySource(self, source):
        cur = self.db.cursor()
        cur.execute('SELECT * FROM data WHERE source = ?', source)
        rows = cur.fetchall()
        if rows is None:
            print('[WARNING] Data fetchall returned 0 entries.')
            return None
        try:
            for row in rows:
                yield Data(*row)
        except:
            raise Exception(f'[ERROR] Error while fetching all Data for {source}')

    def write(self, data):
        cur = self.db.cursor()
        query = 'INSERT INTO data VALUES(?, ?, ?, ?, ?)'
        cur.execute(query, data.toTupel())
        self.db.connection.commit()

    def getLatestBySetOriginSource(self, set, origin, sourceid):
        cur = self.db.cursor()
        # Todo safe query
        cur.execute(f'SELECT * FROM data WHERE sourceId = {sourceid} AND originId = {origin} AND setId={set} ORDER BY timestamp DESC LIMIT 1')
        return Data(*cur.fetchone())

    def getDataBySourceAndSet(self, source: Source, set: int):
        cur = self.db.cursor()
        query = 'SELECT * FROM data WHERE sourceId=? AND originId=? AND setId=? ORDER BY timestamp DESC LIMIT 1'
        cur.execute(query, (source.id, source.origin, set))
        result = cur.fetchone()
        return Data(*result)