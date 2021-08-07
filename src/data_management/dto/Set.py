from dataclasses import dataclass


@dataclass
class Set:
    __slots__ = ['id', 'start_time_ms', 'end_time_ms']
    id: int
    start_time_ms: int
    end_time_ms: int
