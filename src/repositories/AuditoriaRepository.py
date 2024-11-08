from src.database.db_postgresql import get_connection
import traceback
from src.utils.Logger import Logger


class AuditoriaRepository:

    @staticmethod
    def get_all():
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select audi.id_auditoria, audi.parcial, audi.nombre_tabla, audi.tipo_tabla_tipo_operacion, audi.codigo_tabla_tipo_operacion, audi.id_registro, audi.descripcion, audi.fecha_operacion, audi.usuario_operacion, to_sentence(tip_ope.descripcion) tipo_operacion from fauditoria audi left join ftabla tip_ope on tip_ope.id_tabla = audi.tipo_tabla_tipo_operacion and tip_ope.id_valor = audi.codigo_tabla_tipo_operacion order by audi.id_auditoria")
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_auditoria': registro[0],
                        'parcial': registro[1],
                        'nombre_tabla': registro[2],
                        'tipo_tabla_tipo_operacion': registro[3],
                        'codigo_tabla_tipo_operacion': registro[4],
                        'id_registro': registro[5],
                        'descripcion': registro[6],
                        'fecha_operacion': registro[7],
                        'usuario_operacion': registro[8],
                        'tipo_operacion': registro[9]
                    }
                    registro_list.append(registro_dict)
                return registro_list
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return None
        finally:
            if connection:
                connection.close()

    @staticmethod
    def get_by_id(identificador):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select audi.id_auditoria, audi.parcial, audi.nombre_tabla, audi.tipo_tabla_tipo_operacion, audi.codigo_tabla_tipo_operacion, audi.id_registro, audi.descripcion, audi.fecha_operacion, audi.usuario_operacion, to_sentence(tip_ope.descripcion) tipo_operacion from fauditoria audi left join ftabla tip_ope on tip_ope.id_tabla = audi.tipo_tabla_tipo_operacion and tip_ope.id_valor = audi.codigo_tabla_tipo_operacion where audi.id_auditoria = %s order by audi.id_auditoria", (identificador,))
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_auditoria': registro[0],
                        'parcial': registro[1],
                        'nombre_tabla': registro[2],
                        'tipo_tabla_tipo_operacion': registro[3],
                        'codigo_tabla_tipo_operacion': registro[4],
                        'id_registro': registro[5],
                        'descripcion': registro[6],
                        'fecha_operacion': registro[7],
                        'usuario_operacion': registro[8],
                        'tipo_operacion': registro[9]
                    }
                    registro_list.append(registro_dict)
                return registro_list
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return None
        finally:
            if connection:
                connection.close()

    @staticmethod
    def create(registro):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO fauditoria (nombre_tabla, tipo_tabla_tipo_operacion, codigo_tabla_tipo_operacion, id_registro, descripcion, fecha_operacion, usuario_operacion) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id_auditoria, parcial",
                    (registro.nombre_tabla, registro.tipo_tabla_tipo_operacion, registro.codigo_tabla_tipo_operacion, registro.id_registro, registro.descripcion, registro.fecha_operacion, registro.usuario_operacion)
                )
                identificador_expe = cursor.fetchone()[0]
                identificador_parc = cursor.fetchone()[1]
                connection.commit()
                return identificador_expe
        except Exception as ex:
            connection.rollback()
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return None
        finally:
            if connection:
                connection.close()

    @staticmethod
    def update(registro):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE fauditoria SET descripcion = %s WHERE id_auditoria = %s AND parcial = %s",
                    (registro.descripcion, registro.id_auditoria, registro.parcial)
                )
                connection.commit()
                return cursor.rowcount > 0
        except Exception as ex:
            connection.rollback()
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return False
        finally:
            if connection:
                connection.close()
