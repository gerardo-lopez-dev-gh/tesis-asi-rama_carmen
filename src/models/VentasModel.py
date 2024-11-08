class Ventas:
    def __init__(self, id_venta, id_cliente, fecha_venta, cantidad_vendida, precio_total, moneda) -> None:
        self.id_venta = id_venta
        self.id_cliente = id_cliente
        self.fecha_venta = fecha_venta
        self.cantidad_vendida = cantidad_vendida
        self.precio_total = precio_total
        self.moneda = moneda

    def to_json(self):
        return {
            'id_venta': self.id_venta,
            'id_cliente': self.id_cliente,
            'fecha_venta': self.fecha_venta,
            'cantidad_vendida': self.cantidad_vendida,
            'precio_total': self.precio_total,
            'moneda': self.moneda
        }
