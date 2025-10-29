from fastapi import HTTPException, status
from sqlmodel import Session, select
from models import Libro, LibroCreate, LibroUpdate, Autor, AutorCreate, AutorUpdate


def crear_libro(session: Session, new_libro: LibroCreate):
    libro = Libro.from_orm(new_libro)
    session.add(libro)
    session.commit()
    session.refresh(libro)
    return libro

def listar_libros(session: Session, genero: str = None, codigo: int = None):
    query = select(Libro)
    if genero:
        query = query.where(Libro.genero == genero)
    if codigo:
        query = query.where(Libro.id == codigo)
    return session.exec(query).all()

def obtener_libro(session: Session, libro_id: int):
    libro = session.get(Libro, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro

def actualizar_libro(session: Session, libro_id: int, datos: LibroUpdate):
    libro = session.get(Libro, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    libro_data = datos.dict(exclude_unset=True)
    for key, value in libro_data.items():
        setattr(libro, key, value)
    session.add(libro)
    session.commit()
    session.refresh(libro)
    return libro

def eliminar_libro(session: Session, libro_id: int):
    libro = session.get(Libro, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    session.delete(libro)
    session.commit()
    return {"message": "Libro eliminado exitosamente"}

def autor_del_libro(session: Session, libro_id: int):
    libro = session.get(Libro, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    autor = session.get(Autor, libro.autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    return autor


def crear_autor(session: Session, new_autor: AutorCreate):
    autor = Autor.from_orm(new_autor)
    session.add(autor)
    session.commit()
    session.refresh(autor)
    return autor

def listar_autores(session: Session, nacionalidad: str = None):
    query = select(Autor)
    if nacionalidad:
        query = query.where(Autor.nacionalidad == nacionalidad)
    return session.exec(query).all()

def obtener_autor(session: Session, autor_id: int):
    autor = session.get(Autor, autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    return autor

def actualizar_autor(session: Session, autor_id: int, datos: AutorUpdate):
    autor = session.get(Autor, autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    autor_data = datos.dict(exclude_unset=True)
    for key, value in autor_data.items():
        setattr(autor, key, value)
    session.add(autor)
    session.commit()
    session.refresh(autor)
    return autor

def eliminar_autor(session: Session, autor_id: int):
    autor = session.get(Autor, autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    session.delete(autor)
    session.commit()
    return {"message": "Autor eliminado exitosamente"}
