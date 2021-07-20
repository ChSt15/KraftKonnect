class SqlInsertError(Exception):
    def __init__(self, object, table: str) -> None:
        self.object = object
        self.table = table
        super().__init__(f'Could not insert {object.__repr__()} in {table}.')
