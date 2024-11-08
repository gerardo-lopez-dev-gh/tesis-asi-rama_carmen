from src.database.db_postgresql import get_connection
import traceback
from src.utils.Logger import Logger


class HistorialMedicoRepository:

    @staticmethod
    def get_all():
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select id_historial, id_animal, descripcion, fecha from fhistoriales_medicos order by id_historial")
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_historial': registro[0],
                        'id_animal': registro[1],
                        'descripcion': registro[2],
                        'fecha': registro[3]
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
                cursor.execute("select id_historial, id_animal, descripcion, fecha from fhistoriales_medicos where id_historial = %s order by id_historial", identificador)
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_historial': registro[0],
                        'id_animal': registro[1],
                        'descripcion': registro[2],
                        'fecha': registro[3]
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
                    "INSERT INTO fhistoriales_medicos (descripcion, fecha, id_animal) VALUES (%s, %s, %s) RETURNING id_historial",
                    (registro.descripcion, registro.fecha, registro.id_animal)
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
                    "UPDATE fhistoriales_medicos SET descripcion = %s, fecha = %s WHERE id_historial = %s",
                    (registro.descripcion, registro.fecha, registro.id_historial)
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
