from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .SQLURL import SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL) # creates the connection

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)   # sets the session up to talk to the db

Base = declarative_base()  # all models to define tables must extend Base class

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
