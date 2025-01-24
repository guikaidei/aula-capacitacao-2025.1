from use_cases.admin.auth.logout.logout_use_case import LogoutUseCase
from repositories.admin_repository import AdminRepository

from fastapi import FastAPI, Request, Response
from fastapi import APIRouter

router = APIRouter()

admin_repository = AdminRepository()

logout_use_case = LogoutUseCase()

@router.get("/admin/auth/logout")
def admin_logout(response: Response, request: Request):
    return logout_use_case.execute(response, request)