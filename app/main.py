from fastapi import FastAPI, Depends

from app import SQL_URL
from app.routers import system
from sqlmodel import SQLModel, create_engine, Session
from typing import Annotated
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(system.router)
app.mount("/static", StaticFiles(directory="static"))
connect_args = {"check_same_thread": False}
engine = create_engine(SQL_URL, connect_args=connect_args)

def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

session_dep = Annotated[Session, Depends(get_session)]

@app.on_event("startup")
def on_startup():
    create_db()

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///WaterGarden.db"
# app.config["SECRET_KEY"] = "abc"
# db = SQLAlchemy()


# login_manager = LoginManager()
# login_manager.init_app(app)