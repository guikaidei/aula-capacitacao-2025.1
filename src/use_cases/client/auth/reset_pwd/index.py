from repositories.client_repository import ClientRepository
from fastapi import FastAPI, Request, Response
from use_cases.client.auth.reset_pwd.reset_pwd_use_case import ResetPwdUseCase
from use_cases.client.auth.reset_pwd.reset_pwd_dto import ResetPwdDTO
from fastapi import APIRouter

router = APIRouter()

client_repository = ClientRepository()
reset_pwd_use_case = ResetPwdUseCase(client_repository)

@router.post("/client/auth/reset/pwd")
def reset_pwd(reset_pwd_dto: ResetPwdDTO, response: Response, request: Request):
    return reset_pwd_use_case.execute(reset_pwd_dto, response, request)
    