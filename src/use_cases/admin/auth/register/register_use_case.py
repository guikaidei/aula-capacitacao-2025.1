from repositories.admin_repository import AdminRepository
from use_cases.admin.auth.register.register_dto import RegisterDTO
from fastapi import Request, Response
from entities.admin import Admin

class RegisterUseCase:
    admin_repository = AdminRepository

    def __init__(self, admin_repository: AdminRepository):
        self.admin_repository = admin_repository

    def execute(self, register_dto: RegisterDTO, response: Response, request: Request):
        if not register_dto.name or not register_dto.email or not register_dto.password:
            response.status_code = 406
            return{"status": "error", "message": "Cadastro não realizado, pois falta informações"}

        admin = Admin(**register_dto.model_dump())

        self.admin_repository.save(admin)

        response.status_code = 201

        return{"status": "success", "message": "Cadastro do admin feito com sucesso"}