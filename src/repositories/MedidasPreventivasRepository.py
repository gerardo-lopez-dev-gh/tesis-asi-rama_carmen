from src.database.db_postgresql import get_connection
import traceback
from src.utils.Logger import Logger


class MedidasPreventivasRepository:

    @staticmethod
    def get_all():
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select prev.id_medida, prev.id_animal, prev.tipo_tabla_tipo_medida, prev.codigo_tabla_tipo_medida, to_sentence(prev.descripcion) as descripcion, prev.fecha, to_sentence(tip_med.descripcion) as tipo_medida from fmedidas_preventivas prev left outer join ftabla tip_med on tip_med.id_tabla = prev.tipo_tabla_tipo_medida and tip_med.id_valor = prev.codigo_tabla_tipo_medida order by prev.id_medida, prev.id_animal")
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_medida': registro[0],
                        'id_animal': registro[1],
                        'tipo_tabla_tipo_medida': registro[2],
                        'codigo_tabla_tipo_medida': registro[3],
                        'descripcion': registro[4],
                        'fecha': registro[5],
                        'tipo_medida': registro[6]
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
                cursor.execute("select prev.id_medida, prev.id_animal, prev.tipo_tabla_tipo_medida, prev.codigo_tabla_tipo_medida, to_sentence(prev.descripcion) as descripcion, prev.fecha, to_sentence(tip_med.descripcion) as tipo_medida from fmedidas_preventivas prev left outer join ftabla tip_med on tip_med.id_tabla = prev.tipo_tabla_tipo_medida and tip_med.id_valor = prev.codigo_tabla_tipo_medida where id_medida = %s order by id_medida, id_animal", (identificador,))
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_medida': registro[0],
                        'id_animal': registro[1],
                        'tipo_tabla_tipo_medida': registro[2],
                        'codigo_tabla_tipo_medida': registro[3],
                        'descripcion': registro[4],
                        'fecha': registro[5],
                        'tipo_medida': registro[6]
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
                    "INSERT INTO fmedidas_preventivas (id_animal, tipo_tabla_tipo_medida, codigo_tabla_tipo_medida, descripcion, fecha) VALUES (%s, %s, %s, %s, %s) RETURNING id_medida",
                    (registro.id_animal, registro.tipo_tabla_tipo_medida, registro.codigo_tabla_tipo_medida, registro.descripcion, registro.fecha)
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
                    "UPDATE fmedidas_preventivas SET codigo_tabla_tipo_medida = %s, descripcion = %s WHERE id_medida = %s and id_animal = %s",
                    (registro.codigo_tabla_tipo_medida, registro.descripcion, registro.id_medida, registro.id_animal)
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
