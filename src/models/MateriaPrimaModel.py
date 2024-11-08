class MateriaPrima:
    def __init__(self, id_prima, id_animal, descripcion, fecha_obtencion, cantidad) -> None:
        self.id_prima = id_prima
        self.id_animal = id_animal
        self.descripcion = descripcion
        self.fecha_obtencion = fecha_obtencion
        self.cantidad = cantidad

    def to_json(self):
        return {
            'id_prima': self.id_prima,
            'id_animal': self.id_animal,
            'descripcion': self.descripcion,
            'fecha_obtencion': self.fecha_obtencion,
            'cantidad': self.cantidad
        }
