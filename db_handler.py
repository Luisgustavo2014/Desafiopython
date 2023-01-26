# Handling database
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./movie_database.db"

# creating engine
# Setting check_same_thread to False so that the returned connection may be shared across multiple threads
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# bind – An optional Connectable, will assign the bind attribute on the MetaData instance
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# A simple constructor that allows initialization
Base = declarative_base()




