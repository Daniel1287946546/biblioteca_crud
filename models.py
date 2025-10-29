from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

# ---------- MODELO AUTOR ----------
class AuthorBase(SQLModel):
    name: str
    country: str
    birth_year: int

class Author(AuthorBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    books: List["Book"] = Relationship(back_populates="author", cascade_delete=True)


# ---------- MODELO LIBRO ----------
class BookBase(SQLModel):
    title: str
    isbn: str
    year: int
    copies: int  # número de copias disponibles

class Book(BookBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    author_id: Optional[int] = Field(default=None, foreign_key="author.id")
    author: Optional[Author] = Relationship(back_populates="books")
