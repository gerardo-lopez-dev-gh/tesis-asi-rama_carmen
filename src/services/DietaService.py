from src.models.DietasModel import Dietas
from src.repositories.DietaRepository import DietaRepository


class DietaService:

    @staticmethod
    def get_all_dietas():
        return DietaRepository.get_all()

    @staticmethod
    def get_dieta_by_id(id_dieta):
        return DietaRepository.get_by_id(id_dieta)

    @staticmethod
    def create_dieta(id_animal, codigo_tabla_tipo_dieta, descripcion, fecha_inicio, fecha_fin, tipo_tabla_tipo_dieta=8):
        dieta = Dietas(
            id_dieta=None,
            id_animal=id_animal,
            tipo_tabla_tipo_dieta=tipo_tabla_tipo_dieta,
            codigo_tabla_tipo_dieta=codigo_tabla_tipo_dieta,
            descripcion=descripcion,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin
        )
        return DietaRepository.create(dieta)

    @staticmethod
    def update_dieta(id_dieta, id_animal, codigo_tabla_tipo_dieta, descripcion, fecha_inicio, fecha_fin, tipo_tabla_tipo_dieta=8):
        dieta = Dietas(
            id_dieta=id_dieta,
            id_animal=id_animal,
            tipo_tabla_tipo_dieta=tipo_tabla_tipo_dieta,
            codigo_tabla_tipo_dieta=codigo_tabla_tipo_dieta,
            descripcion=descripcion,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin
        )
        return DietaRepository.update(dieta)

    @staticmethod
    def delete_dieta(id_dieta):
        return DietaRepository.delete(id_dieta)
