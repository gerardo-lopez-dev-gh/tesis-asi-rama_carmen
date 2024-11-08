class ProductoFinal:
    def __init__(self, id_producto_final, descripcion, fecha_produccion, cantidad_producida) -> None:
        self.id_producto_final = id_producto_final
        self.descripcion = descripcion
        self.fecha_produccion = fecha_produccion
        self.cantidad_producida = cantidad_producida

    def to_json(self):
        return {
            'id_producto_final': self.id_producto_final,
            'descripcion': self.descripcion,
            'fecha_produccion': self.fecha_produccion,
            'cantidad_producida': self.cantidad_producida
        }
