import dotenv
from pydantic import BaseModel
from typing import Literal, Optional, List
dotenv.load_dotenv()

class Reservation(BaseModel):
    _id: str
    client: str
    status: Literal["agendada", "em andamento", "finalizada"]
    day: int
    month: int
    year: int
    inicial_time: str
    pessoas: int