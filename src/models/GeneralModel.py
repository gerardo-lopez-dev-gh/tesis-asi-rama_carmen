class General:
    def __init__(self, id_persona, nombre, direccion, telefono, correo_electronico,
                 tipo_tabla_estado_civil, codigo_tabla_estado_civil, tipo_tabla_estado_registro,
                 codigo_tabla_estado_registro, tipo_tabla_tipo_registro, codigo_tabla_tipo_registro,
                 documento, tipo_tabla_tipo_documento, codigo_tabla_tipo_documento) -> None:
        self.id_persona = id_persona
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo_electronico = correo_electronico
        self.tipo_tabla_estado_civil = tipo_tabla_estado_civil
        self.codigo_tabla_estado_civil = codigo_tabla_estado_civil
        self.tipo_tabla_estado_registro = tipo_tabla_estado_registro
        self.codigo_tabla_estado_registro = codigo_tabla_estado_registro
        self.tipo_tabla_tipo_registro = tipo_tabla_tipo_registro
        self.codigo_tabla_tipo_registro = codigo_tabla_tipo_registro
        self.documento = documento
        self.tipo_tabla_tipo_documento = tipo_tabla_tipo_documento
        self.codigo_tabla_tipo_documento = codigo_tabla_tipo_documento

    def to_json(self):
        return {
            'id_persona': self.id_persona,
            'nombre': self.nombre,
            'direccion': self.direccion,
            'telefono': self.telefono,
            'correo_electronico': self.correo_electronico,
            'tipo_tabla_estado_civil': self.tipo_tabla_estado_civil,
            'codigo_tabla_estado_civil': self.codigo_tabla_estado_civil,
            'tipo_tabla_estado_registro': self.tipo_tabla_estado_registro,
            'codigo_tabla_estado_registro': self.codigo_tabla_estado_registro,
            'tipo_tabla_tipo_registro': self.tipo_tabla_tipo_registro,
            'codigo_tabla_tipo_registro': self.codigo_tabla_tipo_registro,
            'documento': self.documento,
            'tipo_tabla_tipo_documento': self.tipo_tabla_tipo_documento,
            'codigo_tabla_tipo_documento': self.codigo_tabla_tipo_documento
        }
