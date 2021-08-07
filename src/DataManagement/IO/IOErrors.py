class SqlInsertError(Exception):
    def __init__(self, object, table: str) -> None:
        self.object = object
        self.table = table
        super().__init__(f'Could not insert {object.__repr__()} in {table}.')


class SqlSelectError(Exception):
    def __init__(self, table: str, function: str, data=None) -> None:
        self.table = table
        self.function = function
        self.data = data
        super().__init__(f'Could not select in {table} with {function}. Query data was {data}')

class SqlDeleteError(Exception):
    def __init__(self, table: str, function: str, data=None) -> None:
        self.table = table
        self.function = function
        self.data = data
        super().__init__(f'Could not delete in {table} with {function}. Query data was {data}')

class SqlUpdateError(Exception):
    def __init__(self, table: str, function: str, data=None) -> None:
        self.table = table
        self.function = function
        self.data = data
        super().__init__(f'Could not update in {table} with {function}. Query data was {data}')