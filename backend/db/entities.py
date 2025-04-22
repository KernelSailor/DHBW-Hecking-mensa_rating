from typing import List
from sqlalchemy import CheckConstraint, String, Boolean, Integer, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"
    email: Mapped[str] = mapped_column(CheckConstraint("email LIKE '%@%'"), primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    ratings: Mapped[List["Rating"]] = relationship(back_populates="user_obj")
    suggestions: Mapped[List["Suggestion"]] = relationship(back_populates="user_obj")

    def __repr__(self) -> str:
        return f"User(email={self.email!r}, name={self.name!r})"

class Dish(Base):
    __tablename__ = "dish"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    vegetarian: Mapped[bool] = mapped_column(Boolean)
    vegan: Mapped[bool] = mapped_column(Boolean)
    gluten: Mapped[bool] = mapped_column(Boolean)
    ratings: Mapped[List["Rating"]] = relationship(back_populates="dish_obj")

    def __repr__(self) -> str:
        return f"Dish(id={self.id!r}, name={self.name!r})"

class Rating(Base):
    __tablename__ = "rating"
    timestamp: Mapped[str] = mapped_column(String(50), primary_key=True)
    user_email: Mapped[str] = mapped_column(ForeignKey("user.email"), primary_key=True)
    stars: Mapped[int] = mapped_column(Integer, CheckConstraint("stars BETWEEN 1 AND 5"))
    comment: Mapped[str] = mapped_column(Text, nullable=True)

    def __repr__(self) -> str:
        return f"Rating(timestamp={self.timestamp!r}, user_email={self.user_email!r}, stars={self.stars!r})"

class Suggestion(Base):
    __tablename__ = "suggestion"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text, nullable=True)
    timestamp: Mapped[str] = mapped_column(String(50))
    user_email: Mapped[str] = mapped_column(ForeignKey("user.email"))
    user_obj: Mapped["User"] = relationship(back_populates="suggestions")

    def __repr__(self) -> str:
        return f"Suggestion(id={self.id!r}, name={self.name!r})"

