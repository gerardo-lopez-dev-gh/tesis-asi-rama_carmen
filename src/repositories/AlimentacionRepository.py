from src.database.db_postgresql import get_connection
import traceback
from src.utils.Logger import Logger


class AlimentacionRepository:

    @staticmethod
    def get_all():
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT ali.id_alimentacion, ali.id_dieta, ali.tipo_tabla_tipo_alimento, ali.codigo_tabla_tipo_alimento, ali.cantidad, ali.fecha, to_sentence(tip_ali.descripcion) as tipo_alimento from falimentacion ali left outer join ftabla tip_ali on tip_ali.id_tabla = ali.tipo_tabla_tipo_alimento and tip_ali.id_valor = ali.codigo_tabla_tipo_alimento order by id_alimentacion")
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_alimentacion': registro[0],
                        'id_dieta': registro[1],
                        'tipo_tabla_tipo_alimento': registro[2],
                        'codigo_tabla_tipo_alimento': registro[3],
                        'cantidad': registro[4],
                        'fecha': registro[5],
                        'tipo_alimento': registro[6]
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
                cursor.execute("select ali.id_alimentacion, ali.id_dieta, ali.tipo_tabla_tipo_alimento, ali.codigo_tabla_tipo_alimento, ali.cantidad, ali.fecha, to_sentence(tip_ali.descripcion) as tipo_alimento from falimentacion ali left outer join ftabla tip_ali on tip_ali.id_tabla = ali.tipo_tabla_tipo_alimento and tip_ali.id_valor = ali.codigo_tabla_tipo_alimento where id_alimentacion = %s order by id_alimentacion", (identificador,))
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_alimentacion': registro[0],
                        'id_dieta': registro[1],
                        'tipo_tabla_tipo_alimento': registro[2],
                        'codigo_tabla_tipo_alimento': registro[3],
                        'cantidad': registro[4],
                        'fecha': registro[5],
                        'tipo_alimento': registro[6]
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
                    "INSERT INTO falimentacion (id_dieta, tipo_tabla_tipo_alimento, codigo_tabla_tipo_alimento, cantidad, fecha) VALUES (%s, %s, %s, %s, %s) RETURNING id_alimentacion",
                    (registro.id_dieta, registro.tipo_tabla_tipo_alimento, registro.codigo_tabla_tipo_alimento, registro.cantidad, registro.fecha)
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
                    "UPDATE falimentacion SET id_dieta = %s, codigo_tabla_tipo_alimento = %s, cantidad = %s, fecha = %s WHERE id_alimentacion = %s",
                    (registro.id_dieta, registro.codigo_tabla_tipo_alimento, registro.cantidad, registro.fecha, registro.id_alimentacion)
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

    @staticmethod
    def delete(identificador):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE falimentacion SET codigo_tabla_estado_registro = 2 WHERE id_alimentacion = %s",
                    (identificador,)
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
