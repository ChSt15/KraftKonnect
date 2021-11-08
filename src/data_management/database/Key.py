from dataclasses import dataclass

from sqlalchemy import Column, Integer, String

from src.data_management.database import Base


@dataclass
class Key(Base):
    __tablename__ = 'key'

    id = Column(Integer)
    name = Column(String)
    source = Column(Integer)
    dimension = Column(Integer)
