from src.models.TablaModel import Tabla
from src.repositories.TablaRepository import TablaRepository


class TablaService:

    @staticmethod
    def get_all_ftablas():
        return TablaRepository.get_all()

    @staticmethod
    def get_ftabla_by_id(id_tabla):
        return TablaRepository.get_by_id(id_tabla)

    @staticmethod
    def get_ftabla_reg_by_id(id_tabla, id_valor):
        return TablaRepository.get_reg_by_id(id_tabla, id_valor)

    @staticmethod
    def create_ftabla(id_tabla, descripcion):
        tabla = Tabla(
            id_tabla=id_tabla,
            id_valor=None,  # Será generado por la base de datos
            descripcion=descripcion,
        )
        return TablaRepository.create(tabla)

    @staticmethod
    def update_ftabla(id_tabla, id_valor, descripcion):
        tabla = Tabla(
            id_tabla=id_tabla,
            id_valor=id_valor,
            descripcion=descripcion
        )
        return TablaRepository.update(tabla)
