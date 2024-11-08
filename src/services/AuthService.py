import traceback
from src.database.db_postgresql import get_connection
from src.utils.Logger import Logger
from src.models.UsuariosModel import Usuarios
from src.utils.Security import generate_token
from functools import wraps
from flask import session, redirect, url_for, flash


class AuthService:

    @classmethod
    def login_user(cls, username, password):
        connection = None
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                # Ejecuta la función que retorna un registro del usuario
                cursor.execute('SELECT * FROM authenticate_user(%s, %s)', (username, password))
                row = cursor.fetchone()

                if row:
                    # Desempaqueta los datos de la fila
                    id_usuario, id_persona, operador, tipo_tabla_estado_registro, codigo_tabla_estado_registro, tipo_tabla_tipo_registro, codigo_tabla_tipo_registro = row

                    # Crea una instancia del modelo Usuarios con los datos obtenidos
                    authenticated_user = Usuarios(
                        id_usuario=int(id_usuario),
                        id_persona=int(id_persona),
                        operador=operador,
                        contrasena=None,  # Por seguridad, no se guarda la contraseña
                        tipo_tabla_estado_registro=tipo_tabla_estado_registro,
                        codigo_tabla_estado_registro=codigo_tabla_estado_registro,
                        tipo_tabla_tipo_registro=tipo_tabla_tipo_registro,
                        codigo_tabla_tipo_registro=codigo_tabla_tipo_registro
                    )
                    # Convierte el objeto a un diccionario para que sea serializable
                    user_data = authenticated_user.to_json()  # Asegúrate de tener un método to_dict en Usuarios

                    # Genera un token para el usuario autenticado
                    token = generate_token(user_data)
                    return token, None
                else:
                    return None, "Usuario o contraseña incorrectos."

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
            return None, str(ex)

        finally:
            if connection:
                connection.close()

    @staticmethod
    def login_required(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'token' not in session:
                flash('Debes iniciar sesión para acceder a esta página.', 'error')
                return redirect(url_for('auth_blueprint.login_form'))
            return f(*args, **kwargs)
        return decorated_function