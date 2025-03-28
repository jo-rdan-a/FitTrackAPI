from fastapi import FastAPI
from controllers.treino_controller import router as treino_router
from controllers.exercicio_controller import router as exercicio_router

app = FastAPI(
    title="FitTrack API",
    description="API para monitoramento de treinos e exercícios",
    version="1.0"
)

# Registrando os routers
app.include_router(treino_router, prefix="/treinos", tags=["Treinos"])
app.include_router(exercicio_router, prefix="/exercicios", tags=["Exercícios"])

@app.get("/")
def root():
    return {"message": "Bem-vindo à FitTrack API"}