from sqlmodel import SQLModel, create_engine, Session

# Base de datos SQLite (se creará automáticamente en el proyecto)
DATABASE_URL = "sqlite:///biblioteca.db"

engine = create_engine(DATABASE_URL, echo=False)

def create_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Session

