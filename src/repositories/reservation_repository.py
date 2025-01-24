import os
import dotenv
from cryptography.fernet import Fernet
from mongoengine import *
from entities.reservation import Reservation
from models.reservation_model import ReservationModel
from models.fields.sensivity_field import SensivityField

dotenv.load_dotenv()

class ReservationRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, reservation: Reservation) -> None:
        reservation_model = ReservationModel()
        reservation_dict = reservation.model_dump()

        for k in ReservationModel.get_normal_fields():
            if k in reservation_dict:
                reservation_model[k] = reservation_dict[k]

        for k in ReservationModel.sensivity_fields:
            reservation_model[k] = SensivityField(fernet=self.fernet, data=reservation_dict[k])

        reservation_model.save()
        return None
    
    def delete(self, reservation_id: str) -> None:
        ReservationModel.objects(id=reservation_id).delete()
        return None
    
    def update(self, reservation_id: str) -> None:
        reservation_model = ReservationModel.objects.with_id(reservation_id)
        
        if reservation_model.status == "agendada":
            reservation_model.status = "finalizada"
        
        reservation_model.save()
        return None

    def get_reservation_by_id(self, reservation_id: str) -> dict:
        reservation = ReservationModel.objects.with_id(reservation_id)
        if not reservation:
            return None
        reservation_dict = reservation.to_mongo().to_dict()
        reservation_dict['_id'] = str(reservation_dict['_id'])
        return reservation_dict
    
    def get_reservations(self) -> list:
        reservations = ReservationModel.objects()
        reservations_list = []
        for reservation in reservations:
            reservation_dict = reservation.to_mongo().to_dict()
            reservation_dict['_id'] = str(reservation_dict['_id'])
            reservations_list.append(reservation_dict)
        return reservations_list
    
    def get_reservations_by_client(self, client_id: str) -> list:
        reservations = ReservationModel.objects(client=client_id)
        reservations_list = []
        for reservation in reservations:
            reservation_dict = reservation.to_mongo().to_dict()
            reservation_dict['_id'] = str(reservation_dict['_id'])
            reservations_list.append(reservation_dict)
        return reservations_list