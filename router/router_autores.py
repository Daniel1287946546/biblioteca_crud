from fastapi import APIRouter, status
from database import engine
import crud
from models import Autor, AutorCreate, AutorUpdate
from sqlmodel import Session

router = APIRouter(prefix="/autores", tags=["Autores"])


@router.post("/", response_model=Autor, status_code=status.HTTP_201_CREATED)
def crear(new_autor: AutorCreate):
    with Session(engine) as session:
        return crud.crear_autor(session, new_autor)


@router.get("/", response_model=list[Autor])
def listar(pais_origen: str = None):
    with Session(engine) as session:
        return crud.listar_autores(session, pais_origen)


@router.get("/{id_autor}", response_model=Autor)
def obtener(id_autor: int):
    with Session(engine) as session:
        return crud.obtener_autor(session, id_autor)


@router.patch("/{id_autor}", response_model=Autor)
def actualizar(id_autor: int, datos: AutorUpdate):
    with Session(engine) as session:
        return crud.actualizar_autor(session, id_autor, datos)


@router.delete("/{id_autor}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar(id_autor: int):
    with Session(engine) as session:
        return crud.eliminar_autor(session, id_autor)

@router.get("/{id_autor}/libros")
def libros_de_autor(id_autor: int):
    with Session(engine) as session:
        return crud.libros_de_autor(session, id_autor)
