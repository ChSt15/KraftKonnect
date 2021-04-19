from src.DataManagement.Database.Connection import Connection
from src.DataManagement.DTO import Data

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

    def put(self, data):
        self.db.insert(data)

    def getLatestByIdAndOrigin(self, sourceid, origin):
        cur = self.db.cursor()
        # TODO WHY DOESNT THIS WORK?
        # cur.execute('SELECT * FROM data WHERE source = ? AND origin = ?', (sourceid, origin))
        cur.execute(f'SELECT * FROM data WHERE source = {sourceid} AND origin = {origin} ORDER BY timestamp DESC LIMIT 1')
        return cur.fetchone()[3]
