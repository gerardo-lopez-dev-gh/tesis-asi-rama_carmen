from src.models.VentasModel import Ventas
from src.repositories.VentasRepository import VentasRepository
from src.services.VentaDetalleService import VentaDetalleService


class VentasService:

    @staticmethod
    def get_all_ventas():
        return VentasRepository.get_all()

    @staticmethod
    def get_venta_by_id(id_venta):
        return VentasRepository.get_by_id(id_venta)

    @staticmethod
    def create_venta(id_cliente, fecha_venta, cantidad_vendida, precio_total, moneda):
        venta = Ventas(
            id_venta=None,
            id_cliente=id_cliente,
            fecha_venta=fecha_venta,
            cantidad_vendida=cantidad_vendida,
            precio_total=precio_total,
            moneda=moneda
        )
        return VentasRepository.create(venta)

    @staticmethod
    def update_venta(id_venta, id_cliente, fecha_venta, cantidad_vendida, precio_total, moneda):
        venta = Ventas(
            id_venta=id_venta,
            id_cliente=id_cliente,
            fecha_venta=fecha_venta,
            cantidad_vendida=cantidad_vendida,
            precio_total=precio_total,
            moneda=moneda
        )
        return VentasRepository.update(venta)

    @staticmethod
    def delete_venta(id_venta):
        return VentasRepository.delete(id_venta)

    @staticmethod
    def update_venta_totals(id_venta, id_cliente, fecha_venta, moneda):

        detalles = VentaDetalleService.get_venta_detalle_by_id(id_venta)

        cantidad_total = sum([detalle['cantidad'] for detalle in detalles])
        precio_total = sum([detalle['precio_unitario'] * detalle['cantidad'] for detalle in detalles])

        # Actualizar los totales de la venta
        VentasService.update_venta(
            id_venta=id_venta,
            id_cliente=id_cliente,
            fecha_venta=fecha_venta,
            cantidad_vendida=cantidad_total,
            precio_total=precio_total,
            moneda=moneda
        )