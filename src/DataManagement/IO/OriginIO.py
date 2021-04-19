from src.DataManagement.Database.Connection import Connection
from src.DataManagement.DTO import Source

class SourceIO:
    def __init__(self):
        self.db = Connection('sources')

    def getCode(self, id):
        cur = self.db.cur()
        cur.execute('SELECT code FROM source WHERE id=?', id)
        # TODO return code

    def getAll(self):
        cur = self.db.cur()
        cur.execute('SELECT * FROM sources')
        rows = cur.fetchall()
        if rows is None:
            print('[LOG] Queried 0 sources.')
            return None
        try:
            for row in rows:
                yield Source(*row)
        except:
            Exception('[ERROR] Error while fetching sources.')