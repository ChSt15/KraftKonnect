from dataclasses import dataclass
from time import time_ns


@dataclass
class Data:
    __slots__ = ['id', 'source_id', 'set_id', 'timestamp', 'value']
    id: int
    source_id: int
    set_id: int
    timestamp: int
    value: str

