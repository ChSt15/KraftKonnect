from dataclasses import dataclass


@dataclass
class Source:
    __slots__ = ['id', 'name', 'description', 'values', 'script']
    id: int
    name: str
    description: str
    values: int
    script: str


