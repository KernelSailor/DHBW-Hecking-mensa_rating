from backend.db.dao import DAO
from backend.db.entities import User
from sqlalchemy.orm import Session
from backend.db.dao import DAO
from sqlalchemy import select

class UserDAO(DAO):
    def insert_user(self, email, name):
        with Session(self.engine) as session:
            user = User(email=email, name=name)
            session.add(user)
            session.commit()
    
    def get_user(self, email):
        with Session(self.engine) as session:
            stmt = select(User).where(User.email == email)
            user = session.scalars(stmt).one()

            if user:
                print(user)
            else:
                print(f'user with email {email} not found')

            return user