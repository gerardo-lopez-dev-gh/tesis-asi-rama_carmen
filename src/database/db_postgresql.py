from decouple import config
import psycopg2
import traceback
from src.utils.Logger import Logger
import os


def create_database_if_not_exists():
    try:
        # Conectar a la base de datos predeterminada 'postgres'
        conn = psycopg2.connect(
            host=config('POSTGRESQL_HOST'),
            port=config('POSTGRESQL_PORT'),
            dbname='postgres',  # Usa la base de datos predeterminada 'postgres'
            user=config('POSTGRESQL_USER'),
            password=config('POSTGRESQL_PASSWORD')
        )
        conn.autocommit = True
        cursor = conn.cursor()

        # Verificar si la base de datos existe
        db_name = config('POSTGRESQL_DB')
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}'")
        exists = cursor.fetchone()

        if not exists:
            # Crear la base de datos si no existe
            cursor.execute(f'CREATE DATABASE {db_name}')
            Logger.add_to_log("info", f"Database '{db_name}' created successfully.")
        else:
            Logger.add_to_log("info", f"Database '{db_name}' already exists.")

        cursor.close()
        conn.close()
    except Exception as ex:
        Logger.add_to_log("error", f"Error creating database: {ex}")
        Logger.add_to_log("error", traceback.format_exc())


def execute_sql_script(script_path):
    try:
        # Conectar a la base de datos deseada
        conn = psycopg2.connect(
            host=config('POSTGRESQL_HOST'),
            port=config('POSTGRESQL_PORT'),
            dbname=config('POSTGRESQL_DB'),
            user=config('POSTGRESQL_USER'),
            password=config('POSTGRESQL_PASSWORD')
        )
        cursor = conn.cursor()

        # Leer y ejecutar el archivo SQL
        with open(script_path, 'r', encoding='utf-8') as file:
            sql = file.read()
            cursor.execute(sql)
            conn.commit()
            Logger.add_to_log("info", f"SQL script '{script_path}' executed successfully.")

        cursor.close()
        conn.close()
    except Exception as ex:
        Logger.add_to_log("error", f"Error executing SQL script: {ex}")
        Logger.add_to_log("error", traceback.format_exc())


def get_connection():
    try:
        # Intentar conectar a la base de datos deseada
        conn = psycopg2.connect(
            host=config('POSTGRESQL_HOST'),
            port=config('POSTGRESQL_PORT'),
            dbname=config('POSTGRESQL_DB'),
            user=config('POSTGRESQL_USER'),
            password=config('POSTGRESQL_PASSWORD')
        )
        return conn
    except psycopg2.OperationalError as e:
        if 'does not exist' in str(e):
            Logger.add_to_log("warning", f"Database does not exist, attempting to create it: {e}")
            create_database_if_not_exists()
            # Intentar conectar nuevamente después de crear la base de datos
            return psycopg2.connect(
                host=config('POSTGRESQL_HOST'),
                port=config('POSTGRESQL_PORT'),
                dbname=config('POSTGRESQL_DB'),
                user=config('POSTGRESQL_USER'),
                password=config('POSTGRESQL_PASSWORD')
            )
        else:
            Logger.add_to_log("error", f"OperationalError: {e}")
            Logger.add_to_log("error", traceback.format_exc())
    except psycopg2.ProgrammingError as e:
        Logger.add_to_log("error", f"ProgrammingError: {e}")
        Logger.add_to_log("error", traceback.format_exc())
    except Exception as ex:
        Logger.add_to_log("error", f"Unexpected error: {ex}")
        Logger.add_to_log("error", traceback.format_exc())


# Ejecutar el script SQL después de crear la base de datos
def setup_database():
    create_database_if_not_exists()
    # Ruta al archivo SQL
    sql_script_path = os.path.join(os.path.dirname(__file__), 'inicial.sql')
    execute_sql_script(sql_script_path)


if __name__ == "__main__":
    setup_database()
