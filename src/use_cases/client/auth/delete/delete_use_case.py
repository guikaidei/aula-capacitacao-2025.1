from repositories.client_repository import ClientRepository
from fastapi import Request, Response

class DeleteClientUseCase:
    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository

    def execute(self, client_id: str, response: Response, request: Request):
        print(client_id)
        client = self.client_repository.find_by_id(client_id)
        try:
            client.delete()
            response.status_code = 204  
            return {"status": "success", "message": "Cliente deletado com sucesso"}
        except Exception as e:
            response.status_code = 404  
            return {"status": "error", "message": "erro ao deletar cliente: " + str(e)}