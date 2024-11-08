class Usuarios:
    def __init__(self, id_usuario, id_persona, operador, contrasena, tipo_tabla_estado_registro,
                 codigo_tabla_estado_registro, tipo_tabla_tipo_registro,
                 codigo_tabla_tipo_registro) -> None:
        self.id_usuario = id_usuario
        self.id_persona = id_persona
        self.operador = operador
        self.contrasena = contrasena
        self.tipo_tabla_estado_registro = tipo_tabla_estado_registro
        self.codigo_tabla_estado_registro = codigo_tabla_estado_registro
        self.tipo_tabla_tipo_registro = tipo_tabla_tipo_registro
        self.codigo_tabla_tipo_registro = codigo_tabla_tipo_registro

    def to_json(self):
        return {
            'id_usuario': self.id_usuario,
            'id_persona': self.id_persona,
            'operador': self.operador,
            'contrasena': self.contrasena,
            'tipo_tabla_estado_registro': self.tipo_tabla_estado_registro,
            'codigo_tabla_estado_registro': self.codigo_tabla_estado_registro,
            'tipo_tabla_tipo_registro': self.tipo_tabla_tipo_registro,
            'codigo_tabla_tipo_registro': self.codigo_tabla_tipo_registro
        }
