from src.repositories.EmpresaRepository import EmpresaRepository


class EmpresaService:

    @staticmethod
    def get_id():
        return EmpresaRepository.get_id()

    @staticmethod
    def get_info():
        return EmpresaRepository.get_info()
