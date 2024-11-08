from src.database.db_postgresql import get_connection
import traceback
from src.utils.Logger import Logger


class VentaDetalleRepository:

    @staticmethod
    def get_all():
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select id_detalle, id_producto_final, id_venta, cantidad, precio_unitario, total_item from fventa_detalle order by id_detalle")
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_detalle': registro[0],
                        'id_producto_final': registro[1],
                        'id_venta': registro[2],
                        'cantidad': registro[3],
                        'precio_unitario': registro[4],
                        'total_item': registro[5]
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
                cursor.execute("select id_detalle, id_producto_final, id_venta, cantidad, precio_unitario, total_item from fventa_detalle where id_venta = %s order by id_detalle", (identificador,))
                registros = cursor.fetchall()

                if not registros:
                    return []

                registro_list = []
                for registro in registros:
                    registro_dict = {
                        'id_detalle': registro[0],
                        'id_producto_final': registro[1],
                        'id_venta': registro[2],
                        'cantidad': registro[3],
                        'precio_unitario': registro[4],
                        'total_item': registro[5]
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
                    "INSERT INTO fventa_detalle (id_producto_final, id_venta, cantidad, precio_unitario, total_item) VALUES (%s, %s, %s, %s, %s) RETURNING id_detalle",
                    (registro.id_producto_final, registro.id_venta, registro.cantidad, registro.precio_unitario, registro.total_item)
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
                    "UPDATE fventa_detalle SET id_producto_final = %s, cantidad = %s, precio_unitario = %s, total_item = %s WHERE id_venta = %s and id_detalle = %s",
                    (registro.id_producto_final, registro.cantidad, registro.precio_unitario, registro.total_item, registro.id_venta, registro.id_detalle)
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
    def delete(id_venta, id_detalle):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "delete from fventa_detalle where id_venta = %s and id_detalle = %s",
                    (id_venta, id_detalle)
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
