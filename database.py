from sqlmodel import SQLModel, create_engine

# ---------- Configuración de la base de datos ----------
sqlite_file_name = "biblioteca.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

# ---------- Creación de tablas ----------
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
