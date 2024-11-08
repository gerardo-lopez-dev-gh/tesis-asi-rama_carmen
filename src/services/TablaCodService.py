from src.models.TablaCodModel import TablaCod
from src.repositories.TablaCodRepository import TablaCodRepository


class TablaCodService:

    @staticmethod
    def get_all_ftablascod():
        return TablaCodRepository.get_all()

    @staticmethod
    def get_ftablacod_by_id(id_tabla):
        return TablaCodRepository.get_by_id(id_tabla)

    @staticmethod
    def create_ftablacod(descripcion):
        tabla_cod = TablaCod(
            id_tabla=None,  # Será generado por la base de datos
            descripcion=descripcion,
        )
        return TablaCodRepository.create(tabla_cod)

    @staticmethod
    def update_ftablacod(id_tabla, descripcion):
        tabla_cod = TablaCod(
            id_tabla=id_tabla,
            descripcion=descripcion
        )
        return TablaCodRepository.update(tabla_cod)
