from src.database.db_postgresql import get_connection
import traceback
from src.utils.Logger import Logger


class TratamientosAplicadosRepository:

    @staticmethod
    def get_all():
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select id_tratamiento_apli, id_tratamiento, id_animal, to_sentence(descripcion) as descripcion, fecha_inicio, fecha_fin, to_sentence(resultado) as resultado from ftratamientos_aplicados order by id_tratamiento_apli, id_tratamiento")
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_tratamiento_apli': registro[0],
                        'id_tratamiento': registro[1],
                        'id_animal': registro[2],
                        'descripcion': registro[3],
                        'fecha_inicio': registro[4],
                        'fecha_fin': registro[5],
                        'resultado': registro[6]
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
                cursor.execute("select id_tratamiento_apli, id_tratamiento, id_animal, to_sentence(descripcion) as descripcion, fecha_inicio, fecha_fin, to_sentence(resultado) as resultado from ftratamientos_aplicados where id_tratamiento_apli = %s order by id_tratamiento_apli, id_tratamiento", (identificador,))
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_tratamiento_apli': registro[0],
                        'id_tratamiento': registro[1],
                        'id_animal': registro[2],
                        'descripcion': registro[3],
                        'fecha_inicio': registro[4],
                        'fecha_fin': registro[5],
                        'resultado': registro[6]
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
                    "INSERT INTO ftratamientos_aplicados (id_tratamiento, id_animal, descripcion, fecha_inicio, fecha_fin, resultado) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id_tratamiento_apli",
                    (registro.id_tratamiento, registro.id_animal, registro.descripcion, registro.fecha_inicio, registro.fecha_fin, registro.resultado)
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
                    "UPDATE ftratamientos_aplicados SET descripcion = %s, fecha_inicio = %s, fecha_fin = %s, resultado = %s WHERE id_tratamiento_apli = %s",
                    (registro.descripcion, registro.fecha_inicio, registro.fecha_fin, registro.resultado, registro.id_tratamiento_apli)
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
