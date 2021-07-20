from dataclasses import dataclass
from time import time_ns


@dataclass
class Data:
    __slots__ = ['id', 'set_id', 'source_id', 'value', 'timestamp']
    id: int
    set_id: int
    source_id: int
    value: str
    timestamp: int
