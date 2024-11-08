from src.models.UsuariosModel import Usuarios
from src.repositories.UserRepository import UserRepository


class UserService:

    @staticmethod
    def get_all_users():
        return UserRepository.get_all()

    @staticmethod
    def get_user_by_id(id_usuario):
        return UserRepository.get_by_id(id_usuario)

    @staticmethod
    def create_user(id_persona, operador, contrasena, codigo_tabla_estado_registro, codigo_tabla_tipo_registro, tipo_tabla_estado_registro=13, tipo_tabla_tipo_registro=2):

        user = Usuarios(
            id_usuario=None,  # Será generado por la base de datos
            id_persona=id_persona,
            operador=operador,
            contrasena=contrasena,
            tipo_tabla_estado_registro=tipo_tabla_estado_registro,
            codigo_tabla_estado_registro=codigo_tabla_estado_registro,
            tipo_tabla_tipo_registro=tipo_tabla_tipo_registro,
            codigo_tabla_tipo_registro=codigo_tabla_tipo_registro
        )
        return UserRepository.create(user)

    @staticmethod
    def update_user(id_usuario, id_persona, operador, contrasena):
        user = Usuarios(
            id_usuario=id_usuario,
            id_persona=id_persona,
            operador=operador,
            contrasena=contrasena,
            tipo_tabla_estado_registro=None,  # No se actualiza este campo
            codigo_tabla_estado_registro=None,  # No se actualiza este campo
            tipo_tabla_tipo_registro=None,  # No se actualiza este campo
            codigo_tabla_tipo_registro=None  # No se actualiza este campo
        )
        return UserRepository.update(user)

    @staticmethod
    def delete_user(id_usuario):
        return UserRepository.delete(id_usuario)
