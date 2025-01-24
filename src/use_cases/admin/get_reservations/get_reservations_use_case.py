from repositories.reservation_repository import ReservationRepository
from fastapi import Request, Response
from entities.reservation import Reservation

class GetReservationsUseCase:
    def __init__(self, reservation_repository: ReservationRepository):
        self.reservation_repository = reservation_repository

    def execute(self, response: Response):

        reservations = self.reservation_repository.get_reservations()
        if not reservations:
            response.status_code = 407
            return {"status": "error"}
        
        response.status_code = 200
        return reservations