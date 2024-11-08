class Produccion:
    def __init__(self, id_produccion, id_prima, id_producto_final, id_animal, cantidad_usada) -> None:
        self.id_produccion = id_produccion
        self.id_prima = id_prima
        self.id_producto_final = id_producto_final
        self.id_animal = id_animal
        self.cantidad_usada = cantidad_usada

    def to_json(self):
        return {
            'id_produccion': self.id_produccion,
            'id_prima': self.id_prima,
            'id_producto_final': self.id_producto_final,
            'id_animal': self.id_animal,
            'cantidad_usada': self.cantidad_usada
        }
