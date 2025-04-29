from typing import List
from datetime import datetime
from sqlalchemy import CheckConstraint, Column, DateTime, String, Integer, Table, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

user_votes = Table(
    "association_table",
    Base.metadata,
    Column("user", ForeignKey("user.email"), primary_key=True),
    Column("suggestion", ForeignKey("suggestion.id"), primary_key=True),
)
'''
class UserVotes(Base):
    __tablename__ = "user_votes"
    user: Mapped[int] = mapped_column(ForeignKey("user.email"), primary_key=True)
    suggestion: Mapped[str] = mapped_column(ForeignKey("suggestion.id"), primary_key=True)

    def __repr__(self) -> str:
        return f"Menu Item(date={self.date!r}, name={self.name!r})"
'''

class User(Base):
    __tablename__ = "user"
    email: Mapped[str] = mapped_column(CheckConstraint("email LIKE '%@%'"), primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    password: Mapped[str]
    
    ratings: Mapped[List["Rating"]] = relationship(back_populates="user_obj")
    suggestions: Mapped[List["Suggestion"]] = relationship(back_populates="user_obj")
    suggestions_voted: Mapped[List["Suggestion"]] = relationship(secondary=user_votes, back_populates="users_voted")

    def __repr__(self) -> str:
        return f"User(email={self.email!r}, name={self.name!r})"
    
class Suggestion(Base):
    __tablename__ = "suggestion"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    timestamp: Mapped[datetime] = mapped_column(DateTime)
    user_email: Mapped[str] = mapped_column(ForeignKey("user.email"))
    user_obj: Mapped["User"] = relationship(back_populates="suggestions")

    users_voted: Mapped[List["User"]] = relationship(secondary=user_votes, back_populates="suggestions_voted")

    def __repr__(self) -> str:
        return f"Suggestion(id={self.id!r}, description={self.description!r})"

class Dish(Base):
    __tablename__ = "dish"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    vegetarian: Mapped[bool]
    vegan: Mapped[bool]
    gluten: Mapped[bool]

    ratings: Mapped[List["Rating"]] = relationship(back_populates="dish_obj")
    menu_items: Mapped[List["MenuItem"]] = relationship(back_populates="dish_obj")

    def __repr__(self) -> str:
        return f"Dish(id={self.id!r}, name={self.name!r})"

class Rating(Base):
    __tablename__ = "rating"
    timestamp: Mapped[str] = mapped_column(String(50), primary_key=True)
    user_email: Mapped[str] = mapped_column(ForeignKey("user.email"), primary_key=True)
    stars: Mapped[int] = mapped_column(Integer, CheckConstraint("stars BETWEEN 1 AND 5"))
    comment: Mapped[str] = mapped_column(Text, nullable=True)
    dish_id: Mapped[int] = mapped_column(ForeignKey("dish.id"))

    dish_obj: Mapped[Dish] = relationship(back_populates="ratings")
    user_obj: Mapped[User] = relationship(back_populates="ratings")

    def __repr__(self) -> str:
        return f"Rating(timestamp={self.timestamp!r}, user_email={self.user_email!r}, stars={self.stars!r})"

class MenuItem(Base):
    __tablename__ = "menu_item"
    date: Mapped[int] = mapped_column(primary_key=True)
    dish_id: Mapped[str] = mapped_column(ForeignKey("dish.id"), primary_key=True)

    dish_obj: Mapped[Dish] = relationship(back_populates="menu_items")
    def __repr__(self) -> str:
        return f"Menu Item(date={self.date!r}, name={self.name!r})"

