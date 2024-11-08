from src.database.db_postgresql import get_connection
import traceback
from src.utils.Logger import Logger


class EmpresaRepository:

    @staticmethod
    def get_id():
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select id_empresa from fempresa")
                id_empresa = cursor.fetchone()[0]
                return id_empresa
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return None
        finally:
            if connection:
                connection.close()

    @staticmethod
    def get_info():
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("select * from fempresa ")
                empresa = cursor.fetchall()
                return empresa
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return None
        finally:
            if connection:
                connection.close()
