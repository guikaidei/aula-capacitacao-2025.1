from repositories.client_repository import ClientRepository
from fastapi import Request, Response
from use_cases.client.auth.reset_pwd.reset_pwd_dto import ResetPwdDTO
from datetime import datetime

class ResetPwdUseCase:
    client_repository: ClientRepository

    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository

    def execute(self, reset_pwd_dto: ResetPwdDTO, response: Response, request: Request):
        check_exists = self.client_repository.find_by_reset_pwd_token(token=reset_pwd_dto.token)

        if (len(check_exists) == 0):
            response.status_code = 404
            return {"status": "error", "message": "Não foi possível achar o cliente com o token fornecido"}

        client = check_exists[0]

        if client.reset_pwd_token_sent_at - datetime.now().timestamp() > 900:
            response.status_code = 400
            return {"status": "error", "message": "O token de redefinição expirou. Por favor, solicite um novo."} 
        
        self.client_repository.update_pwd(client.id, reset_pwd_dto.password)

        self.client_repository.update_reset_pwd_token(email=client.email, sent_at=0, token="")
        
        return {"status": "success", "message": "Senha alterada com sucesso, faça login para poder entrar em sua conta."}