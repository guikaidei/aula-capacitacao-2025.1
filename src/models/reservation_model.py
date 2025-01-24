import os
import dotenv
from cryptography.fernet import Fernet
from mongoengine import Document, StringField, IntField, ListField
dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class ReservationModel(Document):
    sensivity_fields = [
        
    ]

    client = StringField(required=True)
    clientId = StringField(required=True)
    status = StringField(required=True)
    day = IntField(required=True)
    month = IntField(required=True)
    year = IntField(required=True)
    inicial_time = StringField(required=True)
    pessoas = IntField(required=True)

    def get_normal_fields():
        return [i for i in ReservationModel.__dict__.keys() if i[:1] != '_' and i != "sensivity_fields" and i not in ReservationModel.sensivity_fields]