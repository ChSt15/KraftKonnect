from dataclasses import dataclass
from time import time_ns


@dataclass
class Data:
    __slots__ = ['id', 'source_id', 'set_id', 'key', 'value', 'timestamp']
    id: int
    source_id: int
    set_id: int
    key: int
    value: str
    timestamp: int

