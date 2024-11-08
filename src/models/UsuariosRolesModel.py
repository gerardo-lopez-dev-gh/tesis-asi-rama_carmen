class UsuariosRoles:
    def __init__(self, id_usu_rol, id_rol, id_usuario) -> None:
        self.id_usu_rol = id_usu_rol
        self.id_rol = id_rol
        self.id_usuario = id_usuario

    def to_json(self):
        return {
            'id_usu_rol': self.id_usu_rol,
            'id_rol': self.id_rol,
            'id_usuario': self.id_usuario
        }
