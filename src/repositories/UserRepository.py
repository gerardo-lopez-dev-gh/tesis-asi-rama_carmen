from src.database.db_postgresql import get_connection
import traceback
from src.utils.Logger import Logger


class UserRepository:

    @staticmethod
    def get_all():
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT usu.id_usuario, usu.operador, usu.tipo_tabla_estado_registro, usu.codigo_tabla_estado_registro, usu.tipo_tabla_tipo_registro, usu.codigo_tabla_tipo_registro, to_sentence(est_reg.descripcion) as estado_registro, to_sentence(tipo_reg.descripcion) as tipo_registro FROM fusuarios usu left outer join ftabla est_reg on est_reg.id_tabla = usu.tipo_tabla_estado_registro and est_reg.id_valor = usu.codigo_tabla_estado_registro left outer join ftabla tipo_reg on tipo_reg.id_tabla = usu.tipo_tabla_tipo_registro and tipo_reg.id_valor = usu.codigo_tabla_tipo_registro WHERE usu.codigo_tabla_estado_registro = 1 order by usu.id_usuario")
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_usuario': registro[0],
                        'operador': registro[1],
                        'tipo_tabla_estado_registro': registro[2],
                        'codigo_tabla_estado_registro': registro[3],
                        'tipo_tabla_tipo_registro': registro[4],
                        'codigo_tabla_tipo_registro': registro[5],
                        'estado_registro': registro[6],
                        'tipo_registro': registro[7]
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
                cursor.execute("SELECT usu.id_usuario, usu.operador, usu.tipo_tabla_estado_registro, usu.codigo_tabla_estado_registro, usu.tipo_tabla_tipo_registro, usu.codigo_tabla_tipo_registro, to_sentence(est_reg.descripcion) as estado_registro, to_sentence(tipo_reg.descripcion) as tipo_registro FROM fusuarios usu left outer join ftabla est_reg on est_reg.id_tabla = usu.tipo_tabla_estado_registro and est_reg.id_valor = usu.codigo_tabla_estado_registro left outer join ftabla tipo_reg on tipo_reg.id_tabla = usu.tipo_tabla_tipo_registro and tipo_reg.id_valor = usu.codigo_tabla_tipo_registro where usu.id_usuario = %s and usu.codigo_tabla_estado_registro = 1 order by usu.id_usuario", (identificador,))
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_usuario': registro[0],
                        'operador': registro[1],
                        'tipo_tabla_estado_registro': registro[2],
                        'codigo_tabla_estado_registro': registro[3],
                        'tipo_tabla_tipo_registro': registro[4],
                        'codigo_tabla_tipo_registro': registro[5],
                        'estado_registro': registro[6],
                        'tipo_registro': registro[7]
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
                    "INSERT INTO fusuarios (id_persona, operador, contrasena, tipo_tabla_estado_registro, codigo_tabla_estado_registro, tipo_tabla_tipo_registro, codigo_tabla_tipo_registro) VALUES (%s, %s, crypt(%s, gen_salt('bf')), %s, %s, %s, %s) RETURNING id_usuario",
                    (registro.id_persona, registro.operador, registro.contrasena, registro.tipo_tabla_estado_registro, registro.codigo_tabla_estado_registro, registro.tipo_tabla_tipo_registro, registro.codigo_tabla_tipo_registro)
                )
                identificador = cursor.fetchone()[0]
                connection.commit()
                return identificador
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
                    "UPDATE fusuarios SET operador = %s, contrasena = crypt(%s, gen_salt('bf')) WHERE id_usuario = %s and id_persona = %s",
                    (registro.operador, registro.contrasena, registro.id_usuario, registro.id_persona)
                )
                connection.commit()
                return cursor.rowcount > 0  # Retorna True si se actualizó
        except Exception as ex:
            connection.rollback()
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return False
        finally:
            if connection:
                connection.close()

    @staticmethod
    def delete(identificador):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE fusuarios SET codigo_tabla_estado_registro = 2 WHERE id_usuario = %s",
                    (identificador,)
                )
                connection.commit()
                return cursor.rowcount > 0  # Retorna True si se eliminó lógicamente
        except Exception as ex:
            connection.rollback()
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return False
        finally:
            if connection:
                connection.close()
