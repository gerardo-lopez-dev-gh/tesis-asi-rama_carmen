class Dietas:
    def __init__(self, id_dieta, id_animal, tipo_tabla_tipo_dieta, codigo_tabla_tipo_dieta,
                 descripcion, fecha_inicio, fecha_fin) -> None:
        self.id_dieta = id_dieta
        self.id_animal = id_animal
        self.tipo_tabla_tipo_dieta = tipo_tabla_tipo_dieta
        self.codigo_tabla_tipo_dieta = codigo_tabla_tipo_dieta
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def to_json(self):
        return {
            'id_dieta': self.id_dieta,
            'id_animal': self.id_animal,
            'tipo_tabla_tipo_dieta': self.tipo_tabla_tipo_dieta,
            'codigo_tabla_tipo_dieta': self.codigo_tabla_tipo_dieta,
            'descripcion': self.descripcion,
            'fecha_inicio': self.fecha_inicio,
            'fecha_fin': self.fecha_fin
        }
