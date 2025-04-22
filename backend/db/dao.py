from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from backend.db.entities import User
from backend.db.entities import Rating
from backend.db.entities import Base
from sqlalchemy import select
from sqlalchemy import text

class DAO():
    def __init__(self):
        self.engine = create_engine("sqlite+pysqlite:///mensa_rating.db", echo=True)
        Base.metadata.create_all(self.engine)