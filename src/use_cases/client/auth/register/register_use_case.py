from repositories.client_repository import ClientRepository
from use_cases.client.auth.register.register_dto import RegisterDTO
from fastapi import Request, Response
from entities.client import Client

class RegisterUseCase:
    client_repository = ClientRepository

    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository

    def execute(self, register_dto: RegisterDTO, response: Response, request: Request):
        if not register_dto.name or not register_dto.email or not register_dto.password:
            response.status_code = 406
            return{"status": "error", "message": "Cadastro não realizado, pois falta informações"}

        client = Client(**register_dto.model_dump())

        self.client_repository.save(client)

        response.status_code = 201

        return{"status": "success", "message": "Cadastro do cliente feito com sucesso"}