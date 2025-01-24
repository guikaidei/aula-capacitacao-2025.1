from repositories.reservation_repository import ReservationRepository
from .get_reservation_use_case import GetReservationUseCase
from .get_reservations_use_case import GetReservationsUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

get_reservation_use_case = GetReservationUseCase(ReservationRepository())
get_reservations_use_case = GetReservationsUseCase(ReservationRepository())

@router.get("/admin/get-reservation/{reservation_id}")
def get_reservation(reservation_id: str ,response:Response, request:Request):
    return get_reservation_use_case.execute(reservation_id,response, request)

@router.get("/admin/get-reservations")
def get_reservations(response:Response):
    return get_reservations_use_case.execute(response)