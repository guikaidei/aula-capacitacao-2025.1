from repositories.client_repository import ClientRepository
from fastapi import FastAPI, Request, Response
from use_cases.client.auth.send_pwd_recovery_email.send_pwd_recovery_email_use_case import SendPwdRecoveryEmailUseCase
from use_cases.client.auth.send_pwd_recovery_email.send_pwd_recovery_email_dto import SendPwdRecoveryEmailDTO
from fastapi import APIRouter

router = APIRouter()

client_repository = ClientRepository()
send_pwd_recovery_email_use_case = SendPwdRecoveryEmailUseCase(client_repository)

@router.post("/client/auth/pwd/recovery/email")
def send_pwd_recovery_email(send_pwd_recovery_email_dto: SendPwdRecoveryEmailDTO, response: Response, request: Request):
    return send_pwd_recovery_email_use_case.execute(send_pwd_recovery_email_dto, response, request)
    