from fastapi import Response, Request

class CheckSessionValidatyUseCase:
    def execute(self, response: Response, request: Request):
        return {"status":"success", "message": "Autenticação é válida para acessar a página de cliente", "user": request.state.auth_payload}