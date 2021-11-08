from dataclasses import dataclass

from sqlalchemy import Column, Integer

from src.data_management.database import Base


class Set(Base):
    """ Set keeps track of data 'recordings' and stores additional metadata """
    __tablename__ = 'set'

    id = Column(Integer, primary_key=True, autoincrement=True)
    start_time_ms = Column(Integer)
    end_time_ms = Column(Integer)
