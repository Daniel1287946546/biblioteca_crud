from fastapi import APIRouter, status
from database import engine
import crud
from models import Libro, LibroCreate, LibroUpdate, Autor
from sqlmodel import Session

router = APIRouter(prefix="/libros", tags=["Libros"])


@router.post("/", response_model=Libro, status_code=status.HTTP_201_CREATED)
def crear(new_libro: LibroCreate):
    with Session(engine) as session:
        return crud.crear_libro(session, new_libro)


# Ahora listar libros solo por año
@router.get("/", response_model=list[Libro])
def listar(año: int):
    with Session(engine) as session:
        return crud.listar_libros(session, año)


@router.get("/{libro_id}", response_model=Libro)
def obtener(libro_id: int):
    with Session(engine) as session:
        return crud.obtener_libro(session, libro_id)


@router.patch("/{libro_id}", response_model=Libro)
def actualizar(libro_id: int, datos: LibroUpdate):
    with Session(engine) as session:
        return crud.actualizar_libro(session, libro_id, datos)


@router.delete("/{libro_id}")
def eliminar(libro_id: int):
    with Session(engine) as session:
        return crud.eliminar_libro(session, libro_id)


@router.get("/{libro_id}/autor", response_model=Autor)
def autor_del_libro(libro_id: int):
    with Session(engine) as session:
        return crud.autor_del_libro(session, libro_id)
