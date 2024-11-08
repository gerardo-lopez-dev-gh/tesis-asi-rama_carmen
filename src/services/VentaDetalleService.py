from src.models.VentaDetalleModel import VentaDetalle
from src.repositories.VentaDetalleRepository import VentaDetalleRepository


class VentaDetalleService:

    @staticmethod
    def get_all_ventas_detalles():
        return VentaDetalleRepository.get_all()

    @staticmethod
    def get_venta_detalle_by_id(id_venta):
        return VentaDetalleRepository.get_by_id(id_venta)

    @staticmethod
    def create_venta_detalle(id_producto_final, id_venta, cantidad, precio_unitario, total_item):
        venta = VentaDetalle(
            id_detalle=None,
            id_producto_final=id_producto_final,
            id_venta=id_venta,
            cantidad=cantidad,
            precio_unitario=precio_unitario,
            total_item=total_item
        )
        return VentaDetalleRepository.create(venta)

    @staticmethod
    def update_venta_detalle(id_detalle, id_producto_final, id_venta, cantidad, precio_unitario, total_item):
        venta = VentaDetalle(
            id_detalle=id_detalle,
            id_producto_final=id_producto_final,
            id_venta=id_venta,
            cantidad=cantidad,
            precio_unitario=precio_unitario,
            total_item=total_item
        )
        return VentaDetalleRepository.update(venta)

    @staticmethod
    def delete_venta_detalle(id_venta, id_detalle):
        return VentaDetalleRepository.delete(id_venta, id_detalle)
