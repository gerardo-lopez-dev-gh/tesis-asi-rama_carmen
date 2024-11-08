from src.models.GeneralModel import General
from src.repositories.GeneralRepository import GeneralRepository


class GeneralService:

    @staticmethod
    def get_all_persons():
        return GeneralRepository.get_all()

    @staticmethod
    def get_person_by_id(id_persona):
        return GeneralRepository.get_by_id(id_persona)

    @staticmethod
    def get_person_by_name(name):
        return GeneralRepository.get_by_name(name)

    @staticmethod
    def get_person_by_lastname(lastname):
        return GeneralRepository.get_by_lastname(lastname)

    @staticmethod
    def create_person(nombre, direccion, telefono, correo_electronico, codigo_tabla_estado_civil, documento, codigo_tabla_tipo_documento, codigo_tabla_estado_registro, codigo_tabla_tipo_registro, tipo_tabla_estado_civil=1, tipo_tabla_tipo_documento=11, tipo_tabla_estado_registro=13, tipo_tabla_tipo_registro=2):
        person = General(
            id_persona=None,  # Será generado por la base de datos
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            correo_electronico=correo_electronico,
            tipo_tabla_estado_civil=tipo_tabla_estado_civil,
            codigo_tabla_estado_civil=codigo_tabla_estado_civil,
            documento=documento,
            tipo_tabla_tipo_documento=tipo_tabla_tipo_documento,
            codigo_tabla_tipo_documento=codigo_tabla_tipo_documento,
            tipo_tabla_estado_registro=tipo_tabla_estado_registro,
            codigo_tabla_estado_registro=codigo_tabla_estado_registro,
            tipo_tabla_tipo_registro=tipo_tabla_tipo_registro,
            codigo_tabla_tipo_registro=codigo_tabla_tipo_registro
        )
        return GeneralRepository.create(person)

    @staticmethod
    def update_person(id_persona, nombre, direccion, telefono, correo_electronico, codigo_tabla_estado_civil, documento, codigo_tabla_tipo_documento, tipo_tabla_estado_civil=1, tipo_tabla_tipo_documento=11):
        person = General(
            id_persona=id_persona,
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            correo_electronico=correo_electronico,
            tipo_tabla_estado_civil=tipo_tabla_estado_civil,
            codigo_tabla_estado_civil=codigo_tabla_estado_civil,
            documento=documento,
            tipo_tabla_tipo_documento=tipo_tabla_tipo_documento,
            codigo_tabla_tipo_documento=codigo_tabla_tipo_documento,
            tipo_tabla_estado_registro=None,  # No se actualiza este campo
            codigo_tabla_estado_registro=None,  # No se actualiza este campo
            tipo_tabla_tipo_registro=None,  # No se actualiza este campo
            codigo_tabla_tipo_registro=None  # No se actualiza este campo
        )
        return GeneralRepository.update(person)

    @staticmethod
    def delete_person(id_persona):
        return GeneralRepository.delete(id_persona)
