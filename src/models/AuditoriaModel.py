class Auditoria:
    def __init__(self, id_auditoria, parcial, nombre_tabla, tipo_tabla_tipo_operacion,
                 codigo_tabla_tipo_operacion, id_registro, descripcion, fecha_operacion,
                 usuario_operacion) -> None:
        self.id_auditoria = id_autoria
        self.parcial = parcial
        self.nombre_tabla = nombre_tabla
        self.tipo_tabla_tipo_operacion = tipo_tabla_tipo_operacion
        self.codigo_tabla_tipo_operacion = codigo_tabla_tipo_operacion
        self.id_registro = id_registro
        self.descripcion = descripcion
        self.fecha_operacion = fecha_operacion
        self.usuario_operacion = usuario_operacion

    def to_json(self):
        return {
            'id_auditoria': self.id_auditoria,
            'parcial': self.parcial,
            'nombre_tabla': self.nombre_tabla,
            'tipo_tabla_tipo_operacion': self.tipo_tabla_tipo_operacion,
            'codigo_tabla_tipo_operacion': self.codigo_tabla_tipo_operacion,
            'id_registro': self.id_registro,
            'descripcion': self.descripcion,
            'fecha_operacion': self.fecha_operacion,
            'usuario_operacion': self.usuario_operacion
        }
