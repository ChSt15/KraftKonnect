from dataclasses import dataclass


@dataclass
class Source:
    __slots__ = ['id', 'name', 'description', 'script']
    id: int
    name: str
    description: str
    script: str


