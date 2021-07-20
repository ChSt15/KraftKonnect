from dataclasses import dataclass
from time import time_ns


@dataclass
class Data:
    __slots__ = ['id', 'source_id', 'set_id', 'timestamp', 'value_id', 'value']
    id: int
    source_id: int
    set_id: int
    timestamp: int
    value_id: int
    value: str

