import os
import bcrypt
import dotenv
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.admin import Admin
from models.admin_model import AdminModel
from models.fields.sensivity_field import SensivityField

dotenv.load_dotenv()

class AdminRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, admin: Admin) -> None:
        admin_model = AdminModel()
        admin_dict = admin.model_dump()

        for k in AdminModel.get_normal_fields():
            if k not in admin_dict:
                continue
            admin_model[k] = admin_dict[k]

        for k in AdminModel.sensivity_fields:
            admin_model[k] = SensivityField(fernet=self.fernet, data=admin_dict[k])

        admin_model.password = bcrypt.hashpw(
            f'{admin.password}'.encode(),
            bcrypt.gensalt()
        ).decode()

        admin_model.save()

    def find_by_email(self, email: str) -> List[AdminModel]:
        return AdminModel.objects(email=email)

    def find_by_id(self, id: str) -> List[AdminModel]:
        return AdminModel.objects(id=id)

    def update_reset_pwd_token(self, email: str, sent_at: int, token: str) -> None:
        AdminModel.objects(email=email).update(
            set__reset_pwd_token_sent_at=sent_at,
            set__reset_pwd_token=token
        )

    def find_by_reset_pwd_token(self, token: str) -> List[AdminModel]:
        return AdminModel.objects(reset_pwd_token=token)

    def update_pwd(self, id: str, pwd: str) -> None:
        AdminModel.objects(id=id).update(
            set__password=bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()
        )

    def get_name(self, id: str) -> str:
        admin = AdminModel.objects(id=id).first()
        if admin:
            return admin.name

    def get_email(self, id: str) -> str:
        admin = AdminModel.objects(id=id).first()
        if admin:
            return admin.email

    def update_name(self, id: str, name: str) -> None:
        AdminModel.objects(id=id).update(set__name=name)

    def update_email(self, id: str, email: str) -> None:
        AdminModel.objects(id=id).update(set__email=email)