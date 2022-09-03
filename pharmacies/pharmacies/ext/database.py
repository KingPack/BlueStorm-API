import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


PATH_USER = os.getcwd()
DATABASE_CLOUD = 'postgresql+psycopg2://oyudkrmmcjgyxy:59ffb8e1d788030f6be2ab236f68122255aed7cdd781671f29b42316958f37d9@ec2-54-147-36-107.compute-1.amazonaws.com:5432/dae0nh4a3d6lqp'
DATABASE_LOCAL = f'sqlite:///{PATH_USER}/pharmacies/ext/backend_test.db'

engine = create_engine(DATABASE_LOCAL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()