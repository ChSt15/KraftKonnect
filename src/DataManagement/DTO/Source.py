from dataclasses import dataclass


@dataclass
class Source:
    __slots__ = ['id', 'description', 'name', 'script']
    id: int
    description: str
    name: str

