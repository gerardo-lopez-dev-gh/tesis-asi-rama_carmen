class Permisos:
    def __init__(self, id_permiso, nombre_permiso, descripcion) -> None:
        self.id_permiso = id_permiso
        self.nombre_permiso = nombre_permiso
        self.descripcion = descripcion

    def to_json(self):
        return {
            'id_permiso': self.id_permiso,
            'nombre_permiso': self.nombre_permiso,
            'descripcion': self.descripcion
        }
