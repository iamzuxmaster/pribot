from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from pathlib import Path


DB = 'db.sqlite3' 

Base = declarative_base()

BASE_DIR = Path(__file__).resolve().parent.parent

connection_string = "sqlite:///"+os.path.join(BASE_DIR, DB)
engine = create_engine(connection_string, echo=True)
Session = sessionmaker()


# CREATE DATABASE
def create_db():
    Base.metadata.create_all(engine)