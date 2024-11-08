class RolesPermisos:
    def __init__(self, id_rol_perm, id_rol, id_permiso) -> None:
        self.id_rol_perm = id_rol_perm
        self.id_rol = id_rol
        self.id_permiso = id_permiso

    def to_json(self):
        return {
            'id_rol_perm': self.id_rol_perm,
            'id_rol': self.id_rol,
            'id_permiso': self.id_permiso
        }
