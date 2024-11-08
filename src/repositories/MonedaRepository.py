from src.database.db_postgresql import get_connection
import traceback
from src.utils.Logger import Logger


class MonedaRepository:

    @staticmethod
    def get_all():
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select mon.id_moneda, to_sentence(mon.nombre) as nombre, mon.tipo_tabla_tipo_moneda, mon.codigo_tabla_tipo_moneda, to_sentence(tip_moneda.descripcion) tipo_moneda from fmoneda mon left join ftabla tip_moneda on tip_moneda.id_tabla = mon.tipo_tabla_tipo_moneda and tip_moneda.id_valor = mon.codigo_tabla_tipo_moneda order by mon.id_moneda")
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_moneda': registro[0],
                        'nombre': registro[1],
                        'tipo_tabla_tipo_moneda': registro[2],
                        'codigo_tabla_tipo_moneda': registro[3],
                        'tipo_moneda': registro[4]
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
                cursor.execute("select mon.id_moneda, to_sentence(mon.nombre) as nombre, mon.tipo_tabla_tipo_moneda, mon.codigo_tabla_tipo_moneda, to_sentence(tip_moneda.descripcion) tipo_moneda from fmoneda mon left join ftabla tip_moneda on tip_moneda.id_tabla = mon.tipo_tabla_tipo_moneda and tip_moneda.id_valor = mon.codigo_tabla_tipo_moneda where mon.id_moneda = %s order by mon.id_moneda", (identificador,))
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_moneda': registro[0],
                        'nombre': registro[1],
                        'tipo_tabla_tipo_moneda': registro[2],
                        'codigo_tabla_tipo_moneda': registro[3],
                        'tipo_moneda': registro[4]
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
                    "INSERT INTO fmoneda (nombre, tipo_tabla_tipo_moneda, codigo_tabla_tipo_moneda) VALUES (%s, %s, %s) RETURNING id_moneda",
                    (registro.nombre, registro.tipo_tabla_tipo_moneda, registro.codigo_tabla_tipo_moneda)
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
                    "UPDATE fmoneda SET nombre = %s, codigo_tabla_tipo_moneda = %s WHERE id_moneda = %s",
                    (registro.nombre, registro.codigo_tabla_tipo_moneda, registro.id_moneda)
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
