from repositories.reservation_repository import ReservationRepository
from fastapi import Request, Response
from entities.reservation import Reservation

class UpdateReservationUseCase:
    def __init__(self, reservation_repository: ReservationRepository):
        self.reservation_repository = reservation_repository

    def execute(self, reservation_id: str, response: Response, request: Request):

        reservation = self.reservation_repository.update(reservation_id)
        
        response.status_code = 200
        return reservation