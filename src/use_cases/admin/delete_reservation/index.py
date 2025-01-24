from repositories.reservation_repository import ReservationRepository
from .delete_reservation_use_case import DeleteReservationUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

delete_reservation_use_case = DeleteReservationUseCase(ReservationRepository())

@router.delete("/admin/delete-reservation/{reservation_id}")
def delete_reservation(reservation_id: str ,response:Response, request:Request):
    return delete_reservation_use_case.execute(reservation_id,response, request)