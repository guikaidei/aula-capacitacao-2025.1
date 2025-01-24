from repositories.admin_repository import AdminRepository
from fastapi import FastAPI, Request, Response, APIRouter, Depends
from .delete_use_case import DeleteAdminUseCase
from middlewares.validate_admin_auth_token import validade_admin_auth_token

router = APIRouter()

admin_repository = AdminRepository()
delete_admin_use_case = DeleteAdminUseCase(admin_repository)

@router.delete("/admin/delete/{admin_id}", dependencies=[Depends(validade_admin_auth_token)])
def delete_admin(admin_id: str, response: Response, request: Request):
    return delete_admin_use_case.execute(admin_id, response, request)