from enum import Enum
from pydantic import BaseModel

class TipoExercicio(str, Enum):
    CARDIO = "cardio"
    FORCA = "forca"
    MOBILIDADE = "mobilidade"

class Exercicio(BaseModel):
    id: int
    nome: str
    tipo: TipoExercicio
    grupos_musculares: list[str]
    equipamento_necessario: bool
    descricao: str | None = None