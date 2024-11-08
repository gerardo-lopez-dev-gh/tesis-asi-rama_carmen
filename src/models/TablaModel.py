class Tabla:
    def __init__(self, id_tabla, id_valor, descripcion) -> None:
        self.id_tabla = id_tabla
        self.id_valor = id_valor
        self.descripcion = descripcion

    def to_json(self):
        return {
            'id_tabla': self.id_tabla,
            'id_valor': self.id_valor,
            'descripcion': self.descripcion,
        }
