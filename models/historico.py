from datetime import date
from pydantic import BaseModel

class HistoricoProgresso(BaseModel):
    usuario_id: int
    data: date
    peso: float | None
    imc: float | None
    forca_maxima: dict[str, float]  