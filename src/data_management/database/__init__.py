from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_URI = 'sqlite:///../../../database.db'
engine = create_engine(DB_URI, echo=True)
Base = declarative_base()
Session = sessionmaker(engine)

# Load classes
import src.data_management.database.Data
import src.data_management.database.Key
import src.data_management.database.Set
import src.data_management.database.Source
# Build tables
Base.metadata.create_all(engine)