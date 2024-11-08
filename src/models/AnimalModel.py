class Animal:
    def __init__(self, id_animal, id_empresa, tipo_tabla_tipo_animal, codigo_tabla_tipo_animal,
                 fecha_nacimiento, peso, tipo_tabla_estado_salud, codigo_tabla_estado_salud,
                 tipo_tabla_estado_registro, codigo_tabla_estado_registro) -> None:
        self.id_animal = id_animal
        self.id_empresa = id_empresa
        self.tipo_tabla_tipo_animal = tipo_tabla_tipo_animal
        self.codigo_tabla_tipo_animal = codigo_tabla_tipo_animal
        self.fecha_nacimiento = fecha_nacimiento
        self.peso = peso
        self.tipo_tabla_estado_salud = tipo_tabla_estado_salud
        self.codigo_tabla_estado_salud = codigo_tabla_estado_salud
        self.tipo_tabla_estado_registro = tipo_tabla_estado_registro
        self.codigo_tabla_estado_registro = codigo_tabla_estado_registro

    def to_json(self):
        return {
            'id_animal': self.id_animal,
            'id_empresa': self.id_empresa,
            'tipo_tabla_tipo_animal': self.tipo_tabla_tipo_animal,
            'codigo_tabla_tipo_animal': self.codigo_tabla_tipo_animal,
            'fecha_nacimiento': self.fecha_nacimiento,
            'peso': self.peso,
            'tipo_tabla_estado_salud': self.tipo_tabla_estado_salud,
            'codigo_tabla_estado_salud': self.codigo_tabla_estado_salud,
            'tipo_tabla_estado_registro': self.tipo_tabla_estado_registro,
            'codigo_tabla_estado_registro': self.codigo_tabla_estado_registro
        }
