from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from routers import alunos, instrutores, auth, medidas, fichas
from dao.database import engine
from models.models import Base

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

Base.metadata.create_all(bind=engine)

app.include_router(alunos.router)
app.include_router(instrutores.router)
app.include_router(auth.router)
app.include_router(medidas.router)
app.include_router(fichas.router)
