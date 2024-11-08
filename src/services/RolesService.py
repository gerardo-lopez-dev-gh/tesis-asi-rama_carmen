from src.models.RolesModel import Roles
from src.repositories.RolesRepository import RolesRepository


class RolesService:

    @staticmethod
    def get_all_roles():
        return RolesRepository.get_all()

    @staticmethod
    def get_rol_by_id(id_rol):
        return RolesRepository.get_by_id(id_rol)

    @staticmethod
    def create_rol(nombre_rol, descripcion):
        rol = Roles(
            id_rol=None,
            nombre_rol=nombre_rol,
            descripcion=descripcion
        )
        return RolesRepository.create(rol)

    @staticmethod
    def update_rol(id_rol, nombre_rol, descripcion):
        rol = Roles(
            id_rol=id_rol,
            nombre_rol=nombre_rol,
            descripcion=descripcion
        )
        return RolesRepository.update(rol)

    '''@staticmethod
    def delete_rol(id_rol):
        return RolesRepository.delete(id_rol)'''
