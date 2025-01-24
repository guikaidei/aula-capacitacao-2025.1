from repositories.client_repository import ClientRepository
from fastapi import FastAPI, Request, Response, APIRouter, Depends
from .delete_use_case import DeleteClientUseCase
from middlewares.validate_client_auth_token import validade_client_auth_token

router = APIRouter()

client_repository = ClientRepository()
delete_client_use_case = DeleteClientUseCase(client_repository)

@router.delete("/client/delete/{client_id}", dependencies=[Depends(validade_client_auth_token)])
def delete_client(client_id: str, response: Response, request: Request):
    return delete_client_use_case.execute(client_id, response, request)