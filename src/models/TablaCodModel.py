class TablaCod:
    def __init__(self, id_tabla, descripcion) -> None:
        self.id_tabla = id_tabla
        self.descripcion = descripcion

    def to_json(self):
        return {
            'id_tabla': self.id_tabla,
            'descripcion': self.descripcion,
        }
