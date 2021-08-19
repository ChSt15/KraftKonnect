from src.data_management.database.Connection import Connection


class KeyInSetIO:
    def __init__(self):
        self.db = Connection('data')

    def insert(self, key: int, set: int) -> None:
        cur = self.db.cursor()
        query = 'INSERT INTO key_in_set(key, set) VALUES(?, ?)'
        cur.execute(query, (key, set))
        self.db.connection.commit()