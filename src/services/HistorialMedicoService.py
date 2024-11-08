from src.models.HistorialMedicoModel import HistorialesMedicos
from src.repositories.HistorialMedicoRepository import HistorialMedicoRepository


class HistorialMedicoService:

    @staticmethod
    def get_all_historiales():
        return HistorialMedicoRepository.get_all()

    @staticmethod
    def get_historial_by_id(id_historial):
        return HistorialMedicoRepository.get_by_id(id_historial)

    @staticmethod
    def create_historial(id_animal, descripcion, fecha):
        historal = HistorialesMedicos(
            id_historial=None,  # Será generado por la base de datos
            id_animal=id_animal,
            descripcion=descripcion,
            fecha=fecha
        )
        return HistorialMedicoRepository.create(historal)

    @staticmethod
    def update_historial(id_historial, id_animal, descripcion, fecha):
        historal = HistorialesMedicos(
            id_historial=id_historial,
            id_animal=id_animal,
            descripcion=descripcion,
            fecha=fecha
        )
        return HistorialMedicoRepository.update(historal)
