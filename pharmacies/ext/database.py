import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


PATH_USER = os.getcwd()
DATABASE_LOCAL = f'sqlite:///{PATH_USER}/pharmacies/ext/backend_test.db'

engine = create_engine(DATABASE_LOCAL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
