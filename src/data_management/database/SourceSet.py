from dataclasses import dataclass

from sqlalchemy import Column, Integer

from src.data_management.database import Base


class SourceSet(Base):
    """ SourceSet keeps track which sources were recorded in which set """

    __tablename__ = 'source_in_set'

    source = Column(Integer)
    set = Column(Integer)
