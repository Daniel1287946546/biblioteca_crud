from fastapi import FastAPI
from sqlmodel import SQLModel
from database import engine
from router import router_libros, router_autores

app = FastAPI(
    title="Sistema de Gestión de Biblioteca",
    description="API para gestionar libros y autores en la biblioteca",
    version="1.0.0"
)


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


app.include_router(router_libros.router)
app.include_router(router_autores.router)


@app.get("/")
def root():
    return {"message": "Bienvenido al Sistema de Biblioteca 📚"}

