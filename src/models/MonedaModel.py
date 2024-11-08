class Moneda:
    def __init__(self, id_moneda, nombre, tipo_tabla_tipo_moneda, codigo_tabla_tipo_moneda) -> None:
        self.id_moneda = id_moneda
        self.nombre = nombre
        self.tipo_tabla_tipo_moneda = tipo_tabla_tipo_moneda
        self.codigo_tabla_tipo_moneda = codigo_tabla_tipo_moneda

    def to_json(self):
        return {
            'id_moneda': self.id_moneda,
            'nombre': self.nombre,
            'tipo_tabla_tipo_moneda': self.tipo_tabla_tipo_moneda,
            'codigo_tabla_tipo_moneda': self.codigo_tabla_tipo_moneda
        }
