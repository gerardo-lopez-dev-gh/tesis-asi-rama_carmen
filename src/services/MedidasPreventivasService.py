from src.models.MedidasPreventivasModel import MedidasPreventivas
from src.repositories.MedidasPreventivasRepository import MedidasPreventivasRepository


class MedidasPreventivasService:

    @staticmethod
    def get_all_medidas_preventivas():
        return MedidasPreventivasRepository.get_all()

    @staticmethod
    def get_medida_preventiva_by_id(id_medida_preventiva):
        return MedidasPreventivasRepository.get_by_id(id_medida_preventiva)

    @staticmethod
    def create_medida_preventiva(id_animal, codigo_tabla_tipo_medida, descripcion, fecha, tipo_tabla_tipo_medida=10):
        medida_preventiva = MedidasPreventivas(
            id_medida=None,
            id_animal=id_animal,
            tipo_tabla_tipo_medida=tipo_tabla_tipo_medida,
            codigo_tabla_tipo_medida=codigo_tabla_tipo_medida,
            descripcion=descripcion,
            fecha=fecha
        )
        return MedidasPreventivasRepository.create(medida_preventiva)

    @staticmethod
    def update_medida_preventiva(id_medida, id_animal, codigo_tabla_tipo_medida, descripcion, fecha, tipo_tabla_tipo_medida=10):
        medida_preventiva = MedidasPreventivas(
            id_medida=id_medida,
            id_animal=id_animal,
            tipo_tabla_tipo_medida=tipo_tabla_tipo_medida,
            codigo_tabla_tipo_medida=codigo_tabla_tipo_medida,
            descripcion=descripcion,
            fecha=fecha
        )
        return MedidasPreventivasRepository.update(medida_preventiva)

    '''@staticmethod
    def delete_medida_preventiva(id_medida_preventiva):
        return MedidasPreventivasRepository.delete(id_medida_preventiva)'''
