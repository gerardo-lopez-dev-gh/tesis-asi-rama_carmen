from src.database.db_postgresql import get_connection
import traceback
from src.utils.Logger import Logger


class DietaRepository:

    @staticmethod
    def get_all():
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select diet.id_dieta, diet.id_animal, diet.codigo_tabla_tipo_dieta, diet.codigo_tabla_tipo_dieta, diet.descripcion, diet.fecha_inicio, diet.fecha_fin, to_sentence(tip_die.descripcion) as tipo_dieta from fdietas diet left outer join ftabla tip_die on tip_die.id_tabla = diet.tipo_tabla_tipo_dieta and tip_die.id_valor = diet.codigo_tabla_tipo_dieta order by diet.id_dieta")
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_dieta': registro[0],
                        'id_animal': registro[1],
                        'tipo_tabla_tipo_dieta': registro[2],
                        'codigo_tabla_tipo_dieta': registro[3],
                        'descripcion': registro[4],
                        'fecha_inicio': registro[5],
                        'fecha_fin': registro[6],
                        'tipo_dieta': registro[7],
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
                cursor.execute("select diet.id_dieta, diet.id_animal, diet.codigo_tabla_tipo_dieta, diet.codigo_tabla_tipo_dieta, diet.descripcion, diet.fecha_inicio, diet.fecha_fin, to_sentence(tip_die.descripcion) as tipo_dieta from fdietas diet left outer join ftabla tip_die on tip_die.id_tabla = diet.tipo_tabla_tipo_dieta and tip_die.id_valor = diet.codigo_tabla_tipo_dieta where diet.id_dieta = %s order by diet.id_dieta", (identificador,))
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_dieta': registro[0],
                        'id_animal': registro[1],
                        'tipo_tabla_tipo_dieta': registro[2],
                        'codigo_tabla_tipo_dieta': registro[3],
                        'descripcion': registro[4],
                        'fecha_inicio': registro[5],
                        'fecha_fin': registro[6],
                        'tipo_dieta': registro[7],
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
                    "INSERT INTO fdietas (id_animal, tipo_tabla_tipo_dieta, codigo_tabla_tipo_dieta, descripcion, fecha_inicio, fecha_fin) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id_dieta",
                    (registro.id_animal, registro.tipo_tabla_tipo_dieta, registro.codigo_tabla_tipo_dieta, registro.descripcion, registro.fecha_inicio, registro.fecha_fin)
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
                    "UPDATE fdietas SET codigo_tabla_tipo_dieta = %s, descripcion = %s, fecha_inicio = %s, fecha_fin = %s WHERE id_dieta = %s AND id_animal = %s",
                    (registro.codigo_tabla_tipo_dieta, registro.descripcion, registro.fecha_inicio, registro.fecha_fin, registro.id_dieta, registro.id_animal)
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
                    "UPDATE fdietas SET codigo_tabla_estado_registro = 2 WHERE id_dieta = %s",
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
