from repositories.reservation_repository import ReservationRepository
from fastapi import Request, Response
from entities.reservation import Reservation

class GetReservationByClientUseCase:
    def __init__(self, reservation_repository: ReservationRepository):
        self.reservation_repository = reservation_repository

    def execute(self, client_id: str, response: Response, request: Request):

        reservations = self.reservation_repository.get_reservations_by_client(client_id)
        if not reservations:
            response.status_code = 407
            return {"status": "error"}
        
        response.status_code = 200
        return reservations