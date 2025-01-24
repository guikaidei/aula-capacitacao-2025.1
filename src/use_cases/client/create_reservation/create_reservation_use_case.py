from repositories.reservation_repository import ReservationRepository
from fastapi import Request, Response
from entities.reservation import Reservation
from use_cases.client.create_reservation.create_reservation_dto import CreateReservationDTO


class CreateReservationUseCase:
    def __init__(self, reservation_repository: ReservationRepository):
        self.reservation_repository = reservation_repository

    def execute(self, create_reservation_dto: CreateReservationDTO, response: Response, request: Request):

        if not create_reservation_dto.client or not create_reservation_dto.day or not create_reservation_dto.month or not create_reservation_dto.year or not create_reservation_dto.inicial_time:
            response.status_code = 407
            return {"status": "error", "message":"faltam informações"}

        reservation = Reservation(
                client = create_reservation_dto.client,
                status = "agendada",
                day = create_reservation_dto.day,
                month = create_reservation_dto.month,
                year = create_reservation_dto.year,
                inicial_time = create_reservation_dto.inicial_time,
                pessoas = create_reservation_dto.pessoas,
        )
        

        self.reservation_repository.save(reservation)
        response.status_code=201
        return {"status": "success", "message":"Reserva criada"}