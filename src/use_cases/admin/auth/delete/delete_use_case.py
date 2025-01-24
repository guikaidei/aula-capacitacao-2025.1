from repositories.admin_repository import AdminRepository
from fastapi import Request, Response

class DeleteAdminUseCase:
    def __init__(self, admin_repository: AdminRepository):
        self.admin_repository = admin_repository

    def execute(self, admin_id: str, response: Response, request: Request):
        print(admin_id)
        admin = self.admin_repository.find_by_id(admin_id)
        try:
            admin.delete()
            response.status_code = 204  
            return {"status": "success", "message": "Admin deletado com sucesso"}
        except Exception as e:
            response.status_code = 404  
            return {"status": "error", "message": "erro ao deletar admin: " + str(e)}