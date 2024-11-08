from src.database.db_postgresql import get_connection
import traceback
from src.utils.Logger import Logger


class TratamientosRepository:

    @staticmethod
    def get_all():
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select id_tratamiento, to_sentence(descripcion) as descripcion, duracion from ftratamientos order by id_tratamiento")
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_tratamiento': registro[0],
                        'descripcion': registro[1],
                        'duracion': registro[2]
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
                cursor.execute("select id_tratamiento, to_sentence(descripcion) as descripcion, duracion from ftratamientos where id_tratamiento = %s order by id_tratamiento", (identificador,))
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_tratamiento': registro[0],
                        'descripcion': registro[1],
                        'duracion': registro[2]
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
                    "INSERT INTO ftratamientos (descripcion, duracion) VALUES (%s, %s) RETURNING id_tratamiento",
                    (registro.descripcion, registro.duracion)
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
                    "UPDATE ftratamientos SET descripcion = %s, duracion = %s WHERE id_tratamiento = %s",
                    (registro.descripcion, registro.duracion, registro.id_tratamiento)
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
