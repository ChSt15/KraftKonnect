from dataclasses import dataclass


@dataclass
class Key:
    __slots__ = ['id', 'name', 'source', 'dimension']
    id: int
    name: str
    source: int
    dimension: int
