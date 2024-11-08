from flask import Blueprint, request, redirect, url_for, render_template, flash, session
from src.services.AuthService import AuthService

auth_blueprint = Blueprint('auth_blueprint', __name__)


@auth_blueprint.route('/login', methods=['GET'])
def login_form():
    # Renderiza el formulario de inicio de sesión
    return render_template('login/login.html')


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # Limpia la sesión al acceder a la página de login
        session.clear()
        return render_template('login/login.html')  # Renderiza el formulario de inicio de sesión

    if request.method == 'POST':
        data = request.form  # Usa request.form para los datos del formulario
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            flash('Falta el nombre de usuario o la contraseña', 'error')
            return redirect(url_for('auth_blueprint.login_form'))


        token, error = AuthService.login_user(username, password)

        if error:
            flash(error, 'error')
            return redirect(url_for('auth_blueprint.login_form'))

        # Guarda el token en la sesión
        session['token'] = token

        # Redirige al usuario a la página de inicio o a otro menú
        flash('¡Inicio de sesión correcto!', 'success')
        return redirect(url_for('index_blueprint.menu'))


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login2():
    #if 'token' in session:  # Verifica si ya hay un token en la sesión
    #    return redirect(url_for('index_blueprint.menu'))
    if request.method == 'GET':
        session.clear()
        return redirect(url_for('auth_blueprint.login_form'))
    data = request.form  # Usa request.form para los datos del formulario
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        flash('Falta el nombre de usuario o la contraseña', 'error')
        return redirect(url_for('auth_blueprint.login_form'))

    # Llama a AuthService para manejar la lógica de autenticación
    token, error = AuthService.login_user(username, password)

    if error:
        flash(error, 'error')
        return redirect(url_for('auth_blueprint.login_form'))

    #Guarda el token en la sesión si es necesario
    session['token'] = token

    #if error:
    #    flash('Usuario o contraseña incorrectos.', 'error')  # Aquí se envía el mensaje de error
    #    return redirect(url_for('auth_blueprint.login_form'))

    # Redirige al usuario a la página de inicio o a otro menú
    flash('¡Inicio de sesión correcto!', 'success')
    return redirect(url_for('index_blueprint.menu'))

    # Renderiza el formulario de inicio de sesión para GET
    #return render_template('login/login.html')


@auth_blueprint.route('/logout', methods=['GET'])
def logout():
    # Elimina el token de la sesión
    session.pop('token', None)

    # Mensaje de confirmación de que se cerró la sesión
    flash('Has cerrado sesión correctamente.', 'success')

    # Redirige al formulario de inicio de sesión
    return redirect(url_for('auth_blueprint.login_form'))
