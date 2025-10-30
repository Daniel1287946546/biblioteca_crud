from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class LibroBase(SQLModel):
    ISBN: int = Field(description="Número ISBN del libro", unique=True, index=True)
    titulo: str
    genero: str
    editorial: Optional[str] = None
    numero_copias: int = Field(default=1, description="Cantidad de copias disponibles")
    anio_publicacion: int = Field(description="Año de publicación del libro")


class Libro(LibroBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    autor_id: Optional[int] = Field(default=None, foreign_key="autor.id")
    autor: Optional["Autor"] = Relationship(back_populates="libros")


class LibroCreate(LibroBase):
    autor_id: Optional[int] = None


class LibroUpdate(SQLModel):
    ISBN: Optional[int] = None
    titulo: Optional[str] = None
    genero: Optional[str] = None
    editorial: Optional[str] = None
    numero_copias: Optional[int] = None
    anio_publicacion: Optional[int] = None
    autor_id: Optional[int] = None

class AutorBase(SQLModel):
    nombre: str
    pais_origen: str
    anio_nacimiento: int = Field(description="Año de nacimiento del autor")


class Autor(AutorBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    libros: List[Libro] = Relationship(back_populates="autor")


class AutorCreate(AutorBase):
    pass


class AutorUpdate(SQLModel):
    nombre: Optional[str] = None
    pais_origen: Optional[str] = None
    anio_nacimiento: Optional[int] = None


