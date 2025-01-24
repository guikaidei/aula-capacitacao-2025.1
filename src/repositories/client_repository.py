import os
import bcrypt
import dotenv
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.client import Client
from models.client_model import ClientModel
from models.fields.sensivity_field import SensivityField

dotenv.load_dotenv()

class ClientRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, client: Client) -> None:
        client_model = ClientModel()
        client_dict = client.model_dump()

        for k in ClientModel.get_normal_fields():
            if k not in client_dict:
                continue
            client_model[k] = client_dict[k]

        for k in ClientModel.sensivity_fields:
            client_model[k] = SensivityField(fernet=self.fernet, data=client_dict[k])

        client_model.password = bcrypt.hashpw(
            f'{client.password}'.encode(),
            bcrypt.gensalt()
        ).decode()

        client_model.save()

    def find_by_email(self, email: str) -> List[ClientModel]:
        return ClientModel.objects(email=email)

    def find_by_id(self, id: str) -> List[ClientModel]:
        return ClientModel.objects(id=id)

    def update_reset_pwd_token(self, email: str, sent_at: int, token: str) -> None:
        ClientModel.objects(email=email).update(
            set__reset_pwd_token_sent_at=sent_at,
            set__reset_pwd_token=token
        )

    def find_by_reset_pwd_token(self, token: str) -> List[ClientModel]:
        return ClientModel.objects(reset_pwd_token=token)

    def update_pwd(self, id: str, pwd: str) -> None:
        ClientModel.objects(id=id).update(
            set__password=bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()
        )

    def get_name(self, id: str) -> str:
        client = ClientModel.objects(id=id).first()
        if client:
            return client.name

    def get_email(self, id: str) -> str:
        client = ClientModel.objects(id=id).first()
        if client:
            return client.email

    def update_name(self, id: str, name: str) -> None:
        ClientModel.objects(id=id).update(set__name=name)

    def update_email(self, id: str, email: str) -> None:
        ClientModel.objects(id=id).update(set__email=email)