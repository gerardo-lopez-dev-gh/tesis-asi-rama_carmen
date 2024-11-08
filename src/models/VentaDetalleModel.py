class VentaDetalle:
    def __init__(self, id_detalle, id_producto_final, id_venta, cantidad, precio_unitario, total_item) -> None:
        self.id_detalle = id_detalle
        self.id_producto_final = id_producto_final
        self.id_venta = id_venta
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.total_item = total_item

    def to_json(self):
        return {
            'id_detalle': self.id_detalle,
            'id_producto_final': self.id_producto_final,
            'id_venta': self.id_venta,
            'cantidad': self.cantidad,
            'precio_unitario': self.precio_unitario,
            'total_item': self.total_item
        }
