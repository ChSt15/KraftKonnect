from dataclasses import dataclass


@dataclass
class Key:
    __slots__ = ['id', 'name', 'source']
    id: int
    name: str
    source: int
