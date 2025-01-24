from repositories.reservation_repository import ReservationRepository
from .create_reservation_dto import CreateReservationDTO
from .create_reservation_use_case import CreateReservationUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

create_reservation_use_case = CreateReservationUseCase(ReservationRepository())

@router.post("/client/create-reservation")
def create_reservation(create_reservation_dto:CreateReservationDTO, response:Response, request:Request):
    return create_reservation_use_case.execute(create_reservation_dto, response, request)