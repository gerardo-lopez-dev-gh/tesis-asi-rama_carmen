from src.database.db_postgresql import get_connection
import traceback
from src.utils.Logger import Logger


class GeneralRepository:

    @staticmethod
    def get_all():
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select gen.nombre, gen.direccion, gen.telefono, gen.correo_electronico, gen.tipo_tabla_estado_civil, gen.codigo_tabla_estado_civil, gen.documento, gen.tipo_tabla_tipo_documento, gen.codigo_tabla_tipo_documento, gen.id_persona, gen.tipo_tabla_estado_registro, gen.codigo_tabla_estado_registro, gen.tipo_tabla_tipo_registro, gen.codigo_tabla_tipo_registro, to_sentence(civil.descripcion) as estado_civil, to_sentence(documento.descripcion) as tipo_documento, to_sentence(est_reg.descripcion) as estado_registro, to_sentence(tipo_reg.descripcion) as tipo_registro from fgeneral gen left outer join ftabla civil on civil.id_tabla = gen.tipo_tabla_estado_civil and civil.id_valor = gen.codigo_tabla_estado_civil left outer join ftabla documento on documento.id_tabla = gen.tipo_tabla_tipo_documento and documento.id_valor = gen.codigo_tabla_tipo_documento left outer join ftabla est_reg on est_reg.id_tabla = gen.tipo_tabla_estado_registro and est_reg.id_valor = gen.codigo_tabla_estado_registro left outer join ftabla tipo_reg on tipo_reg.id_tabla = gen.tipo_tabla_tipo_registro and tipo_reg.id_valor = gen.codigo_tabla_tipo_registro where gen.tipo_tabla_estado_registro = 13 and gen.codigo_tabla_estado_registro = 1 order by gen.id_persona")
                generals = cursor.fetchall()

                # Verificar si los resultados no están vacíos
                if not generals:
                    return []

                # Convertir los resultados en una lista de diccionarios
                general_list = []
                for gen in generals:
                    general_dict = {
                        'nombre': gen[0],
                        'direccion': gen[1],
                        'telefono': gen[2],
                        'correo_electronico': gen[3],
                        'tipo_tabla_estado_civil': gen[4],
                        'codigo_tabla_estado_civil': gen[5],
                        'documento': gen[6],
                        'tipo_tabla_tipo_documento': gen[7],
                        'codigo_tabla_tipo_documento': gen[8],
                        'id_persona': gen[9],
                        'tipo_tabla_estado_registro': gen[10],
                        'codigo_tabla_estado_registro': gen[11],
                        'tipo_tabla_tipo_registro': gen[12],
                        'codigo_tabla_tipo_registro': gen[13],
                        'estado_civil': gen[14],
                        'tipo_documento': gen[15],
                        'estado_registro': gen[16],
                        'tipo_registro': gen[17]
                    }
                    general_list.append(general_dict)
                return general_list
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
                cursor.execute("select gen.nombre, gen.direccion, gen.telefono, gen.correo_electronico, gen.tipo_tabla_estado_civil, gen.codigo_tabla_estado_civil, gen.documento, gen.tipo_tabla_tipo_documento, gen.codigo_tabla_tipo_documento, gen.id_persona, gen.tipo_tabla_estado_registro, gen.codigo_tabla_estado_registro, gen.tipo_tabla_tipo_registro, gen.codigo_tabla_tipo_registro, to_sentence(civil.descripcion) as estado_civil, to_sentence(documento.descripcion) as tipo_documento, to_sentence(est_reg.descripcion) as estado_registro, to_sentence(tipo_reg.descripcion) as tipo_registro from fgeneral gen left outer join ftabla civil on civil.id_tabla = gen.tipo_tabla_estado_civil and civil.id_valor = gen.codigo_tabla_estado_civil left outer join ftabla documento on documento.id_tabla = gen.tipo_tabla_tipo_documento and documento.id_valor = gen.codigo_tabla_tipo_documento left outer join ftabla est_reg on est_reg.id_tabla = gen.tipo_tabla_estado_registro and est_reg.id_valor = gen.codigo_tabla_estado_registro left outer join ftabla tipo_reg on tipo_reg.id_tabla = gen.tipo_tabla_tipo_registro and tipo_reg.id_valor = gen.codigo_tabla_tipo_registro where gen.tipo_tabla_estado_registro = 13 and gen.codigo_tabla_estado_registro = 1 and gen.id_persona = %s order by gen.id_persona", (identificador,))
                general = cursor.fetchall()

                general_list = []
                for gen in general:
                    general_dict = {
                        'nombre': gen[0],
                        'direccion': gen[1],
                        'telefono': gen[2],
                        'correo_electronico': gen[3],
                        'tipo_tabla_estado_civil': gen[4],
                        'codigo_tabla_estado_civil': gen[5],
                        'documento': gen[6],
                        'tipo_tabla_tipo_documento': gen[7],
                        'codigo_tabla_tipo_documento': gen[8],
                        'id_persona': gen[9],
                        'tipo_tabla_estado_registro': gen[10],
                        'codigo_tabla_estado_registro': gen[11],
                        'tipo_tabla_tipo_registro': gen[12],
                        'codigo_tabla_tipo_registro': gen[13],
                        'estado_civil': gen[14],
                        'tipo_documento': gen[15],
                        'estado_registro': gen[16],
                        'tipo_registro': gen[17]
                    }
                    general_list.append(general_dict)
                return general_list
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return None
        finally:
            if connection:
                connection.close()

    @staticmethod
    def get_by_name(name):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select gen.nombre, gen.direccion, gen.telefono, gen.correo_electronico, gen.tipo_tabla_estado_civil, gen.codigo_tabla_estado_civil, gen.documento, gen.tipo_tabla_tipo_documento, gen.codigo_tabla_tipo_documento, gen.id_persona, gen.tipo_tabla_estado_registro, gen.codigo_tabla_estado_registro, gen.tipo_tabla_tipo_registro, gen.codigo_tabla_tipo_registro, to_sentence(civil.descripcion) as estado_civil, to_sentence(documento.descripcion) as tipo_documento, to_sentence(est_reg.descripcion) as estado_registro, to_sentence(tipo_reg.descripcion) as tipo_registro from fgeneral gen left outer join ftabla civil on civil.id_tabla = gen.tipo_tabla_estado_civil and civil.id_valor = gen.codigo_tabla_estado_civil left outer join ftabla documento on documento.id_tabla = gen.tipo_tabla_tipo_documento and documento.id_valor = gen.codigo_tabla_tipo_documento left outer join ftabla est_reg on est_reg.id_tabla = gen.tipo_tabla_estado_registro and est_reg.id_valor = gen.codigo_tabla_estado_registro left outer join ftabla tipo_reg on tipo_reg.id_tabla = gen.tipo_tabla_tipo_registro and tipo_reg.id_valor = gen.codigo_tabla_tipo_registro where gen.tipo_tabla_estado_registro = 13 and gen.codigo_tabla_estado_registro = 1 and gen.nombre ILIKE %s order by gen.id_persona",  (f'%{name}%',))
                generals = cursor.fetchall()

                general_list = []
                for general in generals:
                    general_dict = {
                        'nombre': general[0],
                        'direccion': general[1],
                        'telefono': general[2],
                        'correo_electronico': general[3],
                        'tipo_tabla_estado_civil': general[4],
                        'codigo_tabla_estado_civil': general[5],
                        'documento': general[6],
                        'tipo_tabla_tipo_documento': general[7],
                        'codigo_tabla_tipo_documento': general[8],
                        'id_persona': general[9],
                        'tipo_tabla_estado_registro': general[10],
                        'codigo_tabla_estado_registro': general[11],
                        'tipo_tabla_tipo_registro': general[12],
                        'codigo_tabla_tipo_registro': general[13],
                        'estado_civil': general[14],
                        'tipo_documento': general[15],
                        'estado_registro': general[16],
                        'tipo_registro': general[17]
                    }
                    general_list.append(general_dict)
                return general_list
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return None
        finally:
            if connection:
                connection.close()

    @staticmethod
    def get_by_lastname(lastname):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select gen.nombre, gen.direccion, gen.telefono, gen.correo_electronico, gen.tipo_tabla_estado_civil, gen.codigo_tabla_estado_civil, gen.documento, gen.tipo_tabla_tipo_documento, gen.codigo_tabla_tipo_documento, gen.id_persona, gen.tipo_tabla_estado_registro, gen.codigo_tabla_estado_registro, gen.tipo_tabla_tipo_registro, gen.codigo_tabla_tipo_registro, to_sentence(civil.descripcion) as estado_civil, to_sentence(documento.descripcion) as tipo_documento, to_sentence(est_reg.descripcion) as estado_registro, to_sentence(tipo_reg.descripcion) as tipo_registro from fgeneral gen left outer join ftabla civil on civil.id_tabla = gen.tipo_tabla_estado_civil and civil.id_valor = gen.codigo_tabla_estado_civil left outer join ftabla documento on documento.id_tabla = gen.tipo_tabla_tipo_documento and documento.id_valor = gen.codigo_tabla_tipo_documento left outer join ftabla est_reg on est_reg.id_tabla = gen.tipo_tabla_estado_registro and est_reg.id_valor = gen.codigo_tabla_estado_registro left outer join ftabla tipo_reg on tipo_reg.id_tabla = gen.tipo_tabla_tipo_registro and tipo_reg.id_valor = gen.codigo_tabla_tipo_registro where gen.tipo_tabla_estado_registro = 13 and gen.codigo_tabla_estado_registro = 1 and gen.nombre ILIKE %s order by gen.id_persona",  (f'%{lastname}%',))
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'nombre': registro[0],
                        'direccion': registro[1],
                        'telefono': registro[2],
                        'correo_electronico': registro[3],
                        'tipo_tabla_estado_civil': registro[4],
                        'codigo_tabla_estado_civil': registro[5],
                        'documento': registro[6],
                        'tipo_tabla_tipo_documento': registro[7],
                        'codigo_tabla_tipo_documento': registro[8],
                        'id_persona': registro[9],
                        'tipo_tabla_estado_registro': registro[10],
                        'codigo_tabla_estado_registro': registro[11],
                        'tipo_tabla_tipo_registro': registro[12],
                        'codigo_tabla_tipo_registro': registro[13],
                        'estado_civil': registro[14],
                        'tipo_documento': registro[15],
                        'estado_registro': registro[16],
                        'tipo_registro': registro[17]
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
                    "INSERT INTO fgeneral (nombre, direccion, telefono, correo_electronico, tipo_tabla_estado_civil, codigo_tabla_estado_civil, documento, tipo_tabla_tipo_documento, codigo_tabla_tipo_documento, tipo_tabla_estado_registro, codigo_tabla_estado_registro, tipo_tabla_tipo_registro, codigo_tabla_tipo_registro) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id_persona",
                    (registro.nombre, registro.direccion, registro.telefono, registro.correo_electronico, registro.tipo_tabla_estado_civil, registro.codigo_tabla_estado_civil, registro.documento, registro.tipo_tabla_tipo_documento, registro.codigo_tabla_tipo_documento, registro.tipo_tabla_estado_registro, registro.codigo_tabla_estado_registro, registro.tipo_tabla_tipo_registro, registro.codigo_tabla_tipo_registro)
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
                    "UPDATE fgeneral SET nombre = %s, direccion = %s, telefono = %s, correo_electronico = %s, codigo_tabla_estado_civil = %s, documento = %s, codigo_tabla_tipo_documento = %s WHERE id_persona = %s",
                    (registro.nombre, registro.direccion, registro.telefono, registro.correo_electronico, registro.codigo_tabla_estado_civil, registro.documento, registro.codigo_tabla_tipo_documento, registro.id_persona)
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
                    "UPDATE fgeneral SET codigo_tabla_estado_registro = 2 WHERE id_persona = %s",
                    identificador
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
