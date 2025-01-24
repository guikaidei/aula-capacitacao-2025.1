from pydantic import BaseModel
from typing import Literal, Optional

class CreateReservationDTO(BaseModel):
    client: str
    status: Literal["agendada", "em andamento", "finalizada"]
    day: int
    month: int
    year: int
    inicial_time: str
    pessoas: int
