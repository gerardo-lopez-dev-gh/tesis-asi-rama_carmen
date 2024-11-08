class MedidasPreventivas:
    def __init__(self, id_medida, id_animal, tipo_tabla_tipo_medida, codigo_tabla_tipo_medida,
                 descripcion, fecha) -> None:
        self.id_medida = id_medida
        self.id_animal = id_animal
        self.tipo_tabla_tipo_medida = tipo_tabla_tipo_medida
        self.codigo_tabla_tipo_medida = codigo_tabla_tipo_medida
        self.descripcion = descripcion
        self.fecha = fecha

    def to_json(self):
        return {
            'id_medida': self.id_medida,
            'id_animal': self.id_animal,
            'tipo_tabla_tipo_medida': self.tipo_tabla_tipo_medida,
            'codigo_tabla_tipo_medida': self.codigo_tabla_tipo_medida,
            'descripcion': self.descripcion,
            'fecha': self.fecha
        }
