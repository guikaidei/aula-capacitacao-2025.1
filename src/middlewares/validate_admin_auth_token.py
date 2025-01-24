import os
import jwt
from fastapi import Request, Response, HTTPException

def validade_admin_auth_token(request: Request, response: Response):
    token = request.cookies.get("admin_auth_token")
    print("asdasda")
    print(token)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    try:
        payload = jwt.decode(token.split(" ")[1], os.getenv("ADMIN_JWT_SECRET"), algorithms=["HS256"])
        admin_id = payload.get("id")
        admin_email = payload.get("email")
        request.state.auth_payload = {"appraiser_id": admin_id, "appraiser_email": admin_email}

    except jwt.PyJWTError:
        response.delete_cookie("admin_auth_token")

        raise HTTPException(status_code=401, detail="Invalid JWT token")
    
    return True