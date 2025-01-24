from use_cases.client.auth.login.login_use_case import LoginUseCase
from repositories.client_repository import ClientRepository
from fastapi import FastAPI, Request, Response
from use_cases.client.auth.login.login_dto import LoginDTO
from fastapi import APIRouter

router = APIRouter()

client_repository = ClientRepository()
login_use_case = LoginUseCase(client_repository)

@router.post("/client/auth/login")
def client_login(client_login_dto: LoginDTO, response: Response, request: Request):
    return login_use_case.execute(client_login_dto, response, request)
    