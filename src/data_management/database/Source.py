from dataclasses import dataclass

from sqlalchemy import Column, Integer, String

from src.data_management.database import Base, Session
from src.data_management.database.Data import Data


class Source(Base):
    """ Source represents one data stream of e.g. a single sensor"""

    __tablename__ = 'source'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    script = Column(String)

    def get_data_write_function(self, time, value):
        with Session() as session:
            data = Data(self.id, time, value)
            session.add(data)

