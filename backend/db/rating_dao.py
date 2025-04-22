from sqlalchemy.orm import Session
from backend.db.dao import DAO
from sqlalchemy import select
from sqlalchemy import text

from backend.db.entities import Rating

class RatingDAO(DAO):
    def insert_rating(self, user, stars):
        with Session(self.engine) as session:
            rating = Rating(stars=stars, user=user.email, user_obj=user)
            session.add(rating)
            session.commit()

    def get_ratings_of_user(self, user):
        with Session(self.engine) as session:
            stmt = select(Rating).from_statement(text(f'SELECT * FROM rating WHERE user = :u'))
            user = session.merge(user)
            #rating = session.execute(stmt, {'u': user.email})
            rating = session.scalars(stmt, {'u': user.email}).all()
            print(rating)
            return rating