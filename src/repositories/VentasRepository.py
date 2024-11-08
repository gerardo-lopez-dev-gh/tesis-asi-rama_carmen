from src.database.db_postgresql import get_connection
import traceback
from src.utils.Logger import Logger


class VentasRepository:

    @staticmethod
    def get_all():
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select id_venta, id_cliente, fecha_venta, cantidad_vendida, precio_total, moneda from fventas order by id_venta")
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_venta': registro[0],
                        'id_cliente': registro[1],
                        'fecha_venta': registro[2],
                        'cantidad_vendida': registro[3],
                        'precio_total': registro[4],
                        'moneda': registro[5]
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
                cursor.execute("select id_venta, id_cliente, fecha_venta, cantidad_vendida, precio_total, moneda from fventas where id_venta = %s order by id_venta", (identificador,))
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_venta': registro[0],
                        'id_cliente': registro[1],
                        'fecha_venta': registro[2],
                        'cantidad_vendida': registro[3],
                        'precio_total': registro[4],
                        'moneda': registro[5]
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
                    "INSERT INTO fventas (id_cliente, fecha_venta, cantidad_vendida, precio_total, moneda) VALUES (%s, %s, %s, %s, %s) RETURNING id_venta",
                    (registro.id_cliente, registro.fecha_venta, registro.cantidad_vendida, registro.precio_total, registro.moneda)
                )
                identificador_expe = cursor.fetchone()[0]
                identificador_parc = cursor.fetchone()[1]
                connection.commit()
                return identificador_expe
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
                    "UPDATE fventas SET cantidad_vendida = %s, precio_total = %s, moneda = %s WHERE id_venta = %s and id_cliente = %s",
                    (registro.cantidad_vendida, registro.precio_total, registro.moneda, registro.id_venta, registro.id_cliente)
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
    def delete(id_venta):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "delete from fventas where id_venta = %s",
                    (id_venta,)
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