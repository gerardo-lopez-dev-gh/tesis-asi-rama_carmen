from src.models.AlimentacionModel import Alimentacion
from src.repositories.AlimentacionRepository import AlimentacionRepository


class AlimentacionService:

    @staticmethod
    def get_all_alimentaciones():
        return AlimentacionRepository.get_all()

    @staticmethod
    def get_alimentacion_by_id(id_alimentacion):
        return AlimentacionRepository.get_by_id(id_alimentacion)

    @staticmethod
    def create_alimentacion(id_dieta, codigo_tabla_tipo_alimento, cantidad, fecha, tipo_tabla_tipo_alimento=9):
        alimentacion = Alimentacion(
            id_alimentacion=None,  # Será generado por la base de datos
            id_dieta=id_dieta,
            tipo_tabla_tipo_alimento=tipo_tabla_tipo_alimento,
            codigo_tabla_tipo_alimento=codigo_tabla_tipo_alimento,
            cantidad=cantidad,
            fecha=fecha
        )
        return AlimentacionRepository.create(alimentacion)

    @staticmethod
    def update_alimentacion(id_alimentacion, id_dieta, codigo_tabla_tipo_alimento, cantidad, fecha, tipo_tabla_tipo_alimento=9):
        alimentacion = Alimentacion(
            id_alimentacion=id_alimentacion,
            id_dieta=id_dieta,
            tipo_tabla_tipo_alimento=tipo_tabla_tipo_alimento,
            codigo_tabla_tipo_alimento=codigo_tabla_tipo_alimento,
            cantidad=cantidad,
            fecha=fecha
        )
        return AlimentacionRepository.update(alimentacion)

    @staticmethod
    def delete_alimentacion(id_alimentacion):
        return AlimentacionRepository.delete(id_alimentacion)
