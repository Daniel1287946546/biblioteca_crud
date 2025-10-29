from fastapi import FastAPI
from database import create_db_and_tables
from routers import authors, books

app = FastAPI(title="Sistema de Gestión de Biblioteca")

# Crear tablas al iniciar el servidor
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Rutas principales
app.include_router(authors.router)
app.include_router(books.router)

@app.get("/")
def root():
    return {"message": "Bienvenido al sistema de gestión de biblioteca 📚"}
