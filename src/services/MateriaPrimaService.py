from src.models.MateriaPrimaModel import MateriaPrima
from src.repositories.MateriaPrimaRepository import MateriaPrimaRepository


class MateriaPrimaService:

    @staticmethod
    def get_all_materias_prima():
        return MateriaPrimaRepository.get_all()

    @staticmethod
    def get_materia_prima_by_id(id_materia):
        return MateriaPrimaRepository.get_by_id(id_materia)

    @staticmethod
    def create_materia_prima(id_animal, descripcion, fecha_obtencion, cantidad):
        materia = MateriaPrima(
            id_prima=None,
            id_animal=id_animal,
            descripcion=descripcion,
            fecha_obtencion=fecha_obtencion,
            cantidad=cantidad
        )
        return MateriaPrimaRepository.create(materia)

    @staticmethod
    def update_materia_prima(id_prima, id_animal, descripcion, fecha_obtencion, cantidad):
        materia = MateriaPrima(
            id_prima=id_prima,
            id_animal=id_animal,
            descripcion=descripcion,
            fecha_obtencion=fecha_obtencion,
            cantidad=cantidad
        )
        return MateriaPrimaRepository.update(materia)

    '''@staticmethod
    def delete_materia(id_materia):
        return MateriaPrimaRepository.delete(id_materia)'''
