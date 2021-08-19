from dataclasses import dataclass
from time import time_ns


@dataclass
class Data:
    __slots__ = ['key', 'time', 'value']
    key: int
    time: int
    value: str

