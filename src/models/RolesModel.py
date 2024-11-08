class Roles:
    def __init__(self, id_rol, nombre_rol, descripcion) -> None:
        self.id_rol = id_rol
        self.nombre_rol = nombre_rol
        self.descripcion = descripcion

    def to_json(self):
        return {
            'id_rol': self.id_rol,
            'nombre_rol': self.nombre_rol,
            'descripcion': self.descripcion
        }