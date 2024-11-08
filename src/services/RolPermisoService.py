from src.models.RolPermisoModel import RolesPermisos
from src.repositories.RolPermisoRepository import RolPermisoRepository


class RolesPermisosService:

    @staticmethod
    def get_all_roles_permisos():
        return RolPermisoRepository.get_all()

    @staticmethod
    def get_rol_permiso_by_id(id_rol_permiso):
        return RolPermisoRepository.get_by_id(id_rol_permiso)

    @staticmethod
    def create_rol_permiso(id_rol, id_permiso):
        rol_permiso = RolesPermisos(
            id_rol_perm=None,
            id_rol=id_rol,
            id_permiso=id_permiso
        )
        return RolPermisoRepository.create(rol_permiso)

    '''@staticmethod
    def update_rol_permiso(id_rol_perm, id_permiso, id_rol):
        rol_permiso = RolesPermisos(
            id_rol_perm=id_rol_perm,
            id_rol=id_rol,
            id_permiso=id_permiso
        )
        return RolPermisoRepository.update(rol_permiso)'''

    '''@staticmethod
    def delete_rol_permiso(id_rol_permiso):
        return RolPermisoRepository.delete(id_rol_permiso)'''
