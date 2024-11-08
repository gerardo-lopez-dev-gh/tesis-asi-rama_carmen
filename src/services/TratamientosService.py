from src.models.TratamientosModel import Tratamientos
from src.repositories.TratamientosRepository import TratamientosRepository


class TratamientosService:

    @staticmethod
    def get_all_tratamientos():
        return TratamientosRepository.get_all()

    @staticmethod
    def get_tratamiento_by_id(id_tabla):
        return TratamientosRepository.get_by_id(id_tabla)

    @staticmethod
    def create_tratamiento(descripcion, duracion):
        tratamiento = Tratamientos(
            id_tratamiento=None,  # Será generado por la base de datos
            descripcion=descripcion,
            duracion=duracion
        )
        return TratamientosRepository.create(tratamiento)

    @staticmethod
    def update_tratamiento(id_tratamiento, descripcion, duracion):
        tratamiento = Tratamientos(
            id_tratamiento=id_tratamiento,
            descripcion=descripcion,
            duracion=duracion
        )
        return TratamientosRepository.update(tratamiento)
