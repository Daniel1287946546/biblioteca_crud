from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class LibroBase(SQLModel):
    codigo: int = Field(description="Código único del libro")
    titulo: str
    genero: str
    editorial: Optional[str] = None

class Libro(LibroBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    autor_id: Optional[int] = Field(default=None, foreign_key="autor.id")
    autor: Optional["Autor"] = Relationship(back_populates="libros")

class LibroCreate(LibroBase):
    autor_id: Optional[int] = None

class LibroUpdate(SQLModel):
    codigo: Optional[int] = None
    titulo: Optional[str] = None
    genero: Optional[str] = None
    editorial: Optional[str] = None
    autor_id: Optional[int] = None

class AutorBase(SQLModel):
    nombre: str
    nacionalidad: str
    edad: Optional[int] = None

class Autor(AutorBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    libros: List[Libro] = Relationship(back_populates="autor")

class AutorCreate(AutorBase):
    pass

class AutorUpdate(SQLModel):
    nombre: Optional[str] = None
    nacionalidad: Optional[str] = None
    edad: Optional[int] = None
