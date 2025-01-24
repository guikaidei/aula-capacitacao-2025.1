import os
import jwt
from fastapi import Request, Response, HTTPException

def validade_client_auth_token(request: Request, response: Response):
    token = request.cookies.get("client_auth_token")

    if not token:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    try:        
        payload = jwt.decode(token.split(" ")[1], os.getenv("CLIENT_JWT_SECRET"), algorithms=["HS256"])
        client_id = payload.get("id")
        client_email = payload.get("email")
        request.state.auth_payload = {"appraiser_id": client_id, "appraiser_email": client_email}

    except jwt.PyJWTError:
        response.delete_cookie("client_auth_token")

        raise HTTPException(status_code=401, detail="Invalid JWT token")
    
    return True