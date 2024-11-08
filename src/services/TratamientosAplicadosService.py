from src.models.TratamientosAplicadosModel import TratamientosAplicados
from src.repositories.TratamientosAplicadosRepository import TratamientosAplicadosRepository


class TratamientosAplicadosService:

    @staticmethod
    def get_all_trata_aplicados():
        return TratamientosAplicadosRepository.get_all()

    @staticmethod
    def get_trata_aplicado_by_id(id_tabla):
        return TratamientosAplicadosRepository.get_by_id(id_tabla)

    @staticmethod
    def create_trata_aplicado(id_tratamiento, id_animal, descripcion, fecha_inicio, fecha_fin, resultado):
        tratamiento = TratamientosAplicados(
            id_tratamiento_apli=None,  # Será generado por la base de datos
            id_tratamiento=id_tratamiento,
            id_animal=id_animal,
            descripcion=descripcion,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            resultado=resultado
        )
        return TratamientosAplicadosRepository.create(tratamiento)

    @staticmethod
    def update_trata_aplicado(id_tratamiento_apli, id_tratamiento, id_animal, descripcion, fecha_inicio, fecha_fin, resultado):
        tratamiento = TratamientosAplicados(
            id_tratamiento_apli=id_tratamiento_apli,
            id_tratamiento=id_tratamiento,
            id_animal=id_animal,
            descripcion=descripcion,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            resultado=resultado
        )
        return TratamientosAplicadosRepository.update(tratamiento)
