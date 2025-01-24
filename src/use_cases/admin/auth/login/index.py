from use_cases.admin.auth.login.login_use_case import LoginUseCase
from repositories.admin_repository import AdminRepository
from fastapi import FastAPI, Request, Response
from use_cases.admin.auth.login.login_dto import LoginDTO
from fastapi import APIRouter

router = APIRouter()

admin_repository = AdminRepository()
login_use_case = LoginUseCase(admin_repository)

@router.post("/admin/auth/login")
def admin_login(admin_login_dto: LoginDTO, response: Response, request: Request):
    return login_use_case.execute(admin_login_dto, response, request)
    