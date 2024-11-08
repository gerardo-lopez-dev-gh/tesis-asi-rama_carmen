from src.database.db_postgresql import get_connection
import traceback
from src.utils.Logger import Logger


class AnimalRepository:

    @staticmethod
    def get_all():
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT ani.id_animal, ani.fecha_nacimiento, ani.tipo_tabla_estado_salud, ani.codigo_tabla_estado_salud, ani.peso, ani.tipo_tabla_tipo_animal, ani.codigo_tabla_tipo_animal, ani.tipo_tabla_estado_registro, ani.codigo_tabla_estado_registro, to_sentence(est_sal.descripcion) as estado_salud, to_sentence(tip_ani.descripcion) as tipo_animal, to_sentence(est_reg.descripcion) as estado_registro from fanimal ani left outer join ftabla est_sal on est_sal.id_tabla = ani.tipo_tabla_estado_salud and est_sal.id_valor = ani.codigo_tabla_estado_salud left outer join ftabla tip_ani on tip_ani.id_tabla = ani.tipo_tabla_tipo_animal and tip_ani.id_valor = ani.codigo_tabla_tipo_animal left outer join ftabla est_reg on est_reg.id_tabla = ani.tipo_tabla_estado_registro and est_reg.id_valor = ani.codigo_tabla_estado_registro where ani.codigo_tabla_estado_registro = 1 order by ani.id_animal")
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_animal': registro[0],
                        'fecha_nacimiento': registro[1],
                        'tipo_tabla_estado_salud': registro[2],
                        'codigo_tabla_estado_salud': registro[3],
                        'peso': registro[4],
                        'tipo_tabla_tipo_animal': registro[5],
                        'codigo_tabla_tipo_animal': registro[6],
                        'tipo_tabla_estado_registro': registro[7],
                        'codigo_tabla_estado_registro': registro[8],
                        'estado_salud': registro[9],
                        'tipo_animal': registro[10],
                        'estado_registro': registro[11]
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
                cursor.execute("select ani.id_animal, ani.fecha_nacimiento, ani.tipo_tabla_estado_salud, ani.codigo_tabla_estado_salud, ani.peso, ani.tipo_tabla_tipo_animal, ani.codigo_tabla_tipo_animal, ani.tipo_tabla_estado_registro, ani.codigo_tabla_estado_registro, to_sentence(est_sal.descripcion) as estado_salud, to_sentence(tip_ani.descripcion) as tipo_animal, to_sentence(est_reg.descripcion) as estado_registro from fanimal ani left outer join ftabla est_sal on est_sal.id_tabla = ani.tipo_tabla_estado_salud and est_sal.id_valor = ani.codigo_tabla_estado_salud left outer join ftabla tip_ani on tip_ani.id_tabla = ani.tipo_tabla_tipo_animal and tip_ani.id_valor = ani.codigo_tabla_tipo_animal left outer join ftabla est_reg on est_reg.id_tabla = ani.tipo_tabla_estado_registro and est_reg.id_valor = ani.codigo_tabla_estado_registro where ani.id_animal = %s and ani.codigo_tabla_estado_registro = 1 order by ani.id_animal", (identificador,))
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_animal': registro[0],
                        'fecha_nacimiento': registro[1],
                        'tipo_tabla_estado_salud': registro[2],
                        'codigo_tabla_estado_salud': registro[3],
                        'peso': registro[4],
                        'tipo_tabla_tipo_animal': registro[5],
                        'codigo_tabla_tipo_animal': registro[6],
                        'tipo_tabla_estado_registro': registro[7],
                        'codigo_tabla_estado_registro': registro[8],
                        'estado_salud': registro[9],
                        'tipo_animal': registro[10],
                        'estado_registro': registro[11]
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
                    "INSERT INTO fanimal (id_empresa, tipo_tabla_tipo_animal, codigo_tabla_tipo_animal, fecha_nacimiento, peso, tipo_tabla_estado_salud, codigo_tabla_estado_salud, tipo_tabla_estado_registro, codigo_tabla_estado_registro) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id_animal",
                    (registro.id_empresa, registro.tipo_tabla_tipo_animal, registro.codigo_tabla_tipo_animal, registro.fecha_nacimiento, registro.peso, registro.tipo_tabla_estado_salud, registro.codigo_tabla_estado_salud, registro.tipo_tabla_estado_registro, registro.codigo_tabla_estado_registro)
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
                    "UPDATE fanimal SET codigo_tabla_tipo_animal = %s, fecha_nacimiento = %s, peso = %s, codigo_tabla_estado_salud = %s WHERE id_animal = %s and id_empresa = %s and tipo_tabla_tipo_animal = 12 and tipo_tabla_estado_salud = 5",
                    (registro.codigo_tabla_tipo_animal, registro.fecha_nacimiento, registro.peso, registro.codigo_tabla_estado_salud, registro.id_animal, registro.id_empresa)
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
                    "UPDATE fanimal SET codigo_tabla_estado_registro = 2 WHERE id_animal = %s",
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
