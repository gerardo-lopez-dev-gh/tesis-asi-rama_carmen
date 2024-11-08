from src.models.AuditoriaModel import Auditoria
from src.repositories.AuditoriaRepository import AuditoriaRepository


class AuditoriaService:

    @staticmethod
    def get_all_auditoria():
        return AuditoriaRepository.get_all()

    @staticmethod
    def get_auditoria_by_id(id_auditoria):
        return AuditoriaRepository.get_by_id(id_auditoria)

    @staticmethod
    def create_auditoria(nombre_tabla, codigo_tabla_tipo_operacion, id_registro, descripcion, fecha_operacion, usuario_operacion, tipo_tabla_tipo_operacion=3):
        auditoria = Auditoria(
            id_auditoria=None,
            parcial=None,
            nombre_tabla=nombre_tabla,
            tipo_tabla_tipo_operacion=tipo_tabla_tipo_operacion,
            codigo_tabla_tipo_operacion=codigo_tabla_tipo_operacion,
            id_registro=id_registro,
            descripcion=descripcion,
            fecha_operacion=fecha_operacion,
            usuario_operacion=usuario_operacion
        )
        return AuditoriaRepository.create(auditoria)

    @staticmethod
    def update_auditoria(id_auditoria, parcial, nombre_tabla, codigo_tabla_tipo_operacion, id_registro, descripcion, fecha_operacion, usuario_operacion, tipo_tabla_tipo_operacion=3):
        auditoria = Auditoria(
            id_auditoria=id_auditoria,
            parcial=parcial,
            nombre_tabla=nombre_tabla,
            tipo_tabla_tipo_operacion=tipo_tabla_tipo_operacion,
            codigo_tabla_tipo_operacion=codigo_tabla_tipo_operacion,
            id_registro=id_registro,
            descripcion=descripcion,
            fecha_operacion=fecha_operacion,
            usuario_operacion=usuario_operacion
        )
        return AuditoriaRepository.update(auditoria)

    '''@staticmethod
    def delete_auditoria(id_auditoria):
        return AuditoriaRepository.delete(id_auditoria)'''
