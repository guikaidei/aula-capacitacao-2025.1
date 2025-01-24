import os
import dotenv
import bcrypt
from cryptography.fernet import Fernet
from mongoengine import Document, StringField, IntField

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class ClientModel(Document):
    sensivity_fields = [
        
    ]

    name = StringField(required=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True, unique=True)

    reset_pwd_token = StringField(default="")
    reset_pwd_token_sent_at = IntField(default=0)

    def get_normal_fields():
        return [
            i for i in ClientModel.__dict__.keys()
            if i[:1] != '_' and i != "sensivity_fields" and i not in ClientModel.sensivity_fields
        ]

    def get_decrypted_field(self, field: str):
        if field not in self.sensivity_fields:
            raise Exception("Field not mapped")
        return fernet.decrypt(getattr(self, field, None).token).decode()

    def check_password_matches(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))