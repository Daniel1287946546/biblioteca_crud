from fastapi import HTTPException, status
from sqlmodel import Session, select
from models import Libro, LibroCreate, LibroUpdate, Autor, AutorCreate, AutorUpdate


def crear_libro(session: Session, new_libro: LibroCreate):
    libro = Libro.from_orm(new_libro)
    session.add(libro)
    session.commit()
    session.refresh(libro)
    return libro


# Ahora listar_libros filtra solo por año
def listar_libros(session: Session, año: int):
    query = select(Libro)
    query = query.where(Libro.año == año)  # filtrado solo por año

    libros = session.exec(query).all()
    if not libros:
        raise HTTPException(status_code=404, detail="No se encontraron libros para ese año")
    return libros


def obtener_libro(session: Session, libro_id: int):
    libro = session.get(Libro, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro


def actualizar_libro(session: Session, libro_id: int, datos: LibroUpdate):
    libro = session.get(Libro, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    for key, value in datos.dict(exclude_unset=True).items():
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


def listar_autores(session: Session, pais_origen: str = None):
    query = select(Autor)
    if pais_origen:
        query = query.where(Autor.pais_origen == pais_origen)

    autores = session.exec(query).all()
    if not autores:
        raise HTTPException(status_code=404, detail="No se encontraron autores con esos filtros")
    return autores


def obtener_autor(session: Session, autor_id: int):
    autor = session.get(Autor, autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    return autor


def actualizar_autor(session: Session, autor_id: int, datos: AutorUpdate):
    autor = session.get(Autor, autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    for key, value in datos.dict(exclude_unset=True).items():
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


def libros_de_autor(session: Session, autor_id: int):
    autor = session.get(Autor, autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    if not autor.libros:
        raise HTTPException(status_code=404, detail="El autor no tiene libros")
    return autor.libros
