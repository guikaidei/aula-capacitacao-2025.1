from repositories.reservation_repository import ReservationRepository
from fastapi import Request, Response
from entities.reservation import Reservation

class DeleteReservationUseCase:
    def __init__(self, reservation_repository: ReservationRepository):
        self.reservation_repository = reservation_repository

    def execute(self, reservation_id: str, response: Response, request: Request):

        reservation = self.reservation_repository.delete(reservation_id)
        
        response.status_code = 204
