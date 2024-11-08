from src.models.UsuariosRolesModel import UsuariosRoles
from src.repositories.UsuariosRolesRepository import UsuarioRolRepository


class UsuariosRolesService:

    @staticmethod
    def get_all_usuarios_roles():
        return UsuarioRolRepository.get_all()

    @staticmethod
    def get_usuario_rol_by_id(id_rol_permiso):
        return UsuarioRolRepository.get_by_id(id_rol_permiso)

    @staticmethod
    def create_usuario_rol(id_rol, id_usuario):
        rol_permiso = UsuariosRoles(
            id_usu_rol=None,
            id_rol=id_rol,
            id_usuario=id_usuario
        )
        return UsuarioRolRepository.create(rol_permiso)

    '''@staticmethod
    def update_usuario_rol(id_usu_rol, id_rol, id_usuario):
        rol_permiso = UsuariosRoles(
            id_usu_rol=id_rol_perm,
            id_rol=id_rol,
            id_usuario=id_usuario
        )
        return UsuarioRolRepository.update(rol_permiso)'''

    '''@staticmethod
    def delete_usuario_rol(id_usu_rol):
        return UsuarioRolRepository.delete(id_usu_rol)'''
