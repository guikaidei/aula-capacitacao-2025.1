from fastapi import Response, Request

class LogoutUseCase:
    def __init__(self):
        pass 

    def execute(self, response: Response, request: Request):


        response.delete_cookie(
            key="admin_auth_token",
            httponly=False,
            secure=True,  
            samesite="None", 
            path="/",
        )

        response.status_code = 200
        return response