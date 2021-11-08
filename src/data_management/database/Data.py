from dataclasses import dataclass
from time import time_ns

from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint

from src.data_management.database import Base


@dataclass
class Data(Base):
    __tablename__ = 'data'

    key = Column(Integer)
    time = Column(Integer)
    value = Column(String)

    __table_args__ = (
        PrimaryKeyConstraint(key, time),
    )