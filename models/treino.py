from pydantic import BaseModel
from typing import Optional
from datetime import date

class Treino(BaseModel):
    id: int
    data: date
    usuario_id: int
    duracao_minutos: int
    observacoes: Optional[str] = None