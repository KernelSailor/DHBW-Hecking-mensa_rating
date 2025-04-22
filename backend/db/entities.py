from typing import List
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"
    email: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    ratings: Mapped[List["Rating"]] = relationship(back_populates="user_obj")

    # ...

    def __repr__(self) -> str:
        return f"User(email={self.email!r}, name={self.name!r})"

class Rating(Base):
    __tablename__ = "rating"
    id: Mapped[int] = mapped_column(primary_key=True)
    user = mapped_column(ForeignKey("user.email"))
    stars: Mapped[int]
    user_obj: Mapped["User"] = relationship(back_populates="ratings")

    # ...

    def __repr__(self) -> str:
        return f"Rating(id={self.id!r}, user_email_address={self.stars!r})"
    
class Dish(Base):
    __tablename__ = "dish"
    id: Mapped[int] = mapped_column(primary_key=True)
    name = mapped_column(String(30))
    # ...

# ...
    
