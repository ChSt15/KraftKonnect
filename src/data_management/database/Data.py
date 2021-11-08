from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint

from src.data_management.database import Base


class Data(Base):
    """ Single data reading received from source. Queried for visualization. """

    __tablename__ = 'data'

    source = Column(Integer, primary_key=True)
    time = Column(Integer, primary_key=True)
    value = Column(String)

    __table_args__ = (
        PrimaryKeyConstraint(source, time),
    )