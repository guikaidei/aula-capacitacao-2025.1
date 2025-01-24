from repositories.reservation_repository import ReservationRepository
from .update_reservation_use_case import UpdateReservationUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

update_reservation_use_case = UpdateReservationUseCase(ReservationRepository())

@router.put("/admin/update-reservation/{reservation_id}")
def update_reservation(reservation_id: str ,response:Response, request:Request):
    return update_reservation_use_case.execute(reservation_id,response, request)