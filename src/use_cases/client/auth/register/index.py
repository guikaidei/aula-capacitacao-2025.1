from use_cases.client.auth.register.register_use_case import RegisterUseCase
from repositories.client_repository import ClientRepository
from fastapi import FastAPI, Request, Response
from use_cases.client.auth.register.register_dto import RegisterDTO
from fastapi import APIRouter

router = APIRouter()

client_repository = ClientRepository()
client_register_use_case = RegisterUseCase(client_repository)

@router.post("/client/auth/register")
def client_register(register_dto: RegisterDTO, response: Response, request: Request):
    return client_register_use_case.execute(register_dto, response, request)
    