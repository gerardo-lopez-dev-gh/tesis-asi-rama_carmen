from config import configurations
from src import init_app
from src.database.db_postgresql import setup_database
from flask import make_response

# Configuración de la aplicación
configuration = configurations['development']

# Configurar la base de datos (crear si no existe y ejecutar scripts)
setup_database()

# Inicializar la aplicación
app = init_app(configuration)


@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    return response


if __name__ == '__main__':
    app.run()
