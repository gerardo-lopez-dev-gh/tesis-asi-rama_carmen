from src.models.MonedaModel import Moneda
from src.repositories.MonedaRepository import MonedaRepository


class MonedaService:

    @staticmethod
    def get_all_monedas():
        return MonedaRepository.get_all()

    @staticmethod
    def get_moneda_by_id(id_rol):
        return MonedaRepository.get_by_id(id_rol)

    @staticmethod
    def create_moneda(nombre, codigo_tabla_tipo_moneda, tipo_tabla_tipo_moneda=15):
        moneda = Moneda(
            id_moneda=None,
            nombre=nombre,
            tipo_tabla_tipo_moneda=tipo_tabla_tipo_moneda,
            codigo_tabla_tipo_moneda=codigo_tabla_tipo_moneda
        )
        return MonedaRepository.create(moneda)

    @staticmethod
    def update_moneda(id_moneda, nombre, codigo_tabla_tipo_moneda, tipo_tabla_tipo_moneda=15):
        moneda = Moneda(
            id_moneda=id_moneda,
            nombre=nombre,
            tipo_tabla_tipo_moneda=tipo_tabla_tipo_moneda,
            codigo_tabla_tipo_moneda=codigo_tabla_tipo_moneda
        )
        return MonedaRepository.update(moneda)

    '''@staticmethod
    def delete_moneda(id_moneda):
        return MonedaRepository.delete(id_moneda)'''
