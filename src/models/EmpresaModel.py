class Empresa:
    def __init__(self, id_empresa, id_propietario, nombre, direccion, telefono, correo_electronico,
                 tipo_tabla_tipo_ganaderia, codigo_tabla_tipo_ganaderia, total_animales) -> None:
        self.id_empresa = id_empresa
        self.id_propietario = id_propietario
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo_electronico = correo_electronico
        self.tipo_tabla_tipo_ganaderia = tipo_tabla_tipo_ganaderia
        self.codigo_tabla_tipo_ganaderia = codigo_tabla_tipo_ganaderia
        self.total_animales = total_animales

    def to_json(self):
        return {
            'id_empresa': self.id_empresa,
            'id_propietario': self.id_propietario,
            'nombre': self.nombre,
            'direccion': self.direccion,
            'telefono': self.telefono,
            'correo_electronico': self.correo_electronico,
            'tipo_tabla_tipo_ganaderia': self.tipo_tabla_tipo_ganaderia,
            'codigo_tabla_tipo_ganaderia': self.codigo_tabla_tipo_ganaderia,
            'total_animales': self.total_animales
        }
