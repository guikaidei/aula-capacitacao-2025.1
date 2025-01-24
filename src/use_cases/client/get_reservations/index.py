from repositories.reservation_repository import ReservationRepository
from .get_reservations_by_client_use_case import GetReservationByClientUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

get_reservation_by_client_use_case = GetReservationByClientUseCase(ReservationRepository())

@router.get("/client/get-reservation/{client_id}")
def get_reservation_by_client(client_id: str ,response:Response, request:Request):
    return get_reservation_by_client_use_case.execute(client_id,response, request)