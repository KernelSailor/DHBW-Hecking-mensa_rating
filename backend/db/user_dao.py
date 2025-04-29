from backend.db.dao import DAO
from backend.db.entities import Suggestion, User
from sqlalchemy.orm import Session
from backend.db.dao import DAO
from sqlalchemy import select
from datetime import datetime

class UserDAO(DAO):
    def insert_user(self, email, name, password):
        with Session(self.engine) as session:
            user = User(email=email, name=name, password=password)
            session.add(user)
            session.commit()

    def delete_user(self, email):
        with Session(self.engine) as session:
            user = self.get_user(email)
            session.delete(user)
            session.commit()
    
    def get_user(self, email):
        with Session(self.engine) as session:
            stmt = select(User).where(User.email == email)
            user = session.scalars(stmt).one()

            return user
        
    def insert_suggestion(self, email, description):
        with Session(self.engine) as session:
            suggestion = Suggestion(description=description, timestamp=datetime.now(), user_email=email)
            user = self.get_user(email)
            user = session.merge(user)
            user.suggestions.append(suggestion)
            session.commit()
