from src.database.db_postgresql import get_connection
import traceback
from src.utils.Logger import Logger


class MateriaPrimaRepository:

    @staticmethod
    def get_all():
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select id_prima, id_animal, to_sentence(descripcion) as descripcion, fecha_obtencion, cantidad from fmateria_prima order by id_prima, id_animal")
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_prima': registro[0],
                        'id_animal': registro[1],
                        'descripcion': registro[2],
                        'fecha_obtencion': registro[3],
                        'cantidad': registro[4]
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
                cursor.execute("select id_prima, id_animal, to_sentence(descripcion) as descripcion, fecha_obtencion, cantidad from fmateria_prima where id_prima = %s order by id_prima, id_animal", (identificador,))
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_prima': registro[0],
                        'id_animal': registro[1],
                        'descripcion': registro[2],
                        'fecha_obtencion': registro[3],
                        'cantidad': registro[4]
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
                    "INSERT INTO fmateria_prima (id_animal, descripcion, fecha_obtencion, cantidad) VALUES (%s, %s, %s, %s) RETURNING id_prima",
                    (registro.id_animal, registro.descripcion, registro.fecha_obtencion, registro.cantidad)
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
                    "UPDATE fmateria_prima SET descripcion = %s, cantidad = %s WHERE id_prima = %s and id_animal = %s",
                    (registro.descripcion, registro.cantidad, registro.id_prima, registro.id_animal)
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
