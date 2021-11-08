from dataclasses import dataclass

from sqlalchemy import Column, Integer, String

from src.data_management.database import Base


@dataclass
class Source(Base):
    __tablename__ = 'source'
    id = Column(Integer)
    name = Column(String)
    description = Column(String)
    script = Column(String)


