from flask import Blueprint, request, redirect, url_for, render_template, flash
from src.services.UserService import UserService
from src.services.AuthService import AuthService


user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('/list', methods=['GET'])
@AuthService.login_required
def list_users():
    users = UserService.get_all_users()
    return render_template('users/list.html', usuarios=users)


@user_blueprint.route('/edit', methods=['GET', 'POST'])
@AuthService.login_required
def edit_user_form():
    if request.method == 'POST':
        id_usuario = request.form.get('id_usuario')
        if not id_usuario:
            flash('ID de usuario no proporcionado', 'error')
            return redirect(url_for('user_blueprint.edit_user_form'))

        usuarios = UserService.get_user_by_id(id_usuario)

        if isinstance(usuarios, list):
            usuarios = usuarios[0] if usuarios else None

        if not usuarios:
            flash('Usuario no encontrado', 'error')
            return redirect(url_for('user_blueprint.edit_user_form'))

        return render_template('users/edit.html', usuario=usuarios)

    return render_template('users/edit.html', usuario=None)


@user_blueprint.route('/view', methods=['GET', 'POST'])
@AuthService.login_required
def view_user():
    filter_value = request.args.get('filter_value', '')
    filter_type = request.args.get('filter_type', 'id')

    if filter_value.strip() == "":
        if 'filter_value' in request.args:
            flash('Debes ingresar un valor de búsqueda', 'error')
        return render_template('users/view.html')

    if filter_type == 'id':
        usuarios = UserService.get_user_by_id(filter_value)
    else:
        flash('Tipo de filtro no válido', 'error')
        return redirect(url_for('user_blueprint.list_users'))

    if not usuarios:
        flash('No se encontraron usuarios', 'error')
        return render_template('users/view.html')

    if isinstance(usuarios, dict):
        usuarios = [usuarios]

    return render_template('users/view.html', usuarios=usuarios)


@user_blueprint.route('/new', methods=['GET'])
@AuthService.login_required
def new_user_form():
    return render_template('users/new.html')


@user_blueprint.route('/create', methods=['POST'])
@AuthService.login_required
def create_user():
    data = request.form
    id_persona = data.get('id_persona')
    operador = data.get('operador')
    contrasena = data.get('contrasena')
    tipo_tabla_estado_registro = 13
    codigo_tabla_estado_registro = 1
    tipo_tabla_tipo_registro = 2
    codigo_tabla_tipo_registro = 5

    if not id_persona or not operador or not contrasena or not codigo_tabla_tipo_registro:
        flash('Faltan datos obligatorios', 'error')
        return redirect(url_for('user_blueprint.new_user_form'))

    id_user = UserService.create_user(
        id_persona=id_persona,
        operador=operador,
        contrasena=contrasena,
        codigo_tabla_estado_registro=codigo_tabla_estado_registro,
        codigo_tabla_tipo_registro=codigo_tabla_tipo_registro,
        tipo_tabla_estado_registro=tipo_tabla_estado_registro,
        tipo_tabla_tipo_registro=tipo_tabla_tipo_registro
    )

    if id_user:
        flash('Usuario creado exitosamente', 'success')
        return redirect(url_for('user_blueprint.view_user'))
    else:
        flash('Error al crear el usuario', 'error')
        return redirect(url_for('user_blueprint.new_user_form'))


@user_blueprint.route('/update/<int:id_usuario>', methods=['POST'])
@AuthService.login_required
def update_user(id_usuario):
    data = request.form
    operador = data.get('operador')
    contrasena = data.get('contrasena')
    id_persona = data.get('id_persona')

    if not operador or not contrasena:
        flash('Faltan datos obligatorios', 'error')
        return redirect(url_for('user_blueprint.edit_user_form', id_usuario=id_usuario))

    success = UserService.update_user(
        id_usuario=id_usuario,
        id_persona=id_persona,
        operador=operador,
        contrasena=contrasena
    )

    if success:
        flash('Usuario actualizado exitosamente', 'success')
        return redirect(url_for('user_blueprint.edit_user_form', id_usuario=id_usuario))
    else:
        flash('Error al actualizar el usuario', 'error')
        return redirect(url_for('user_blueprint.edit_user_form', id_usuario=id_usuario))


@user_blueprint.route('/delete/<int:id_user>', methods=['POST'])
@AuthService.login_required
def delete_user(id_user):
    success = UserService.delete_user(id_user)

    if success:
        flash('Usuario eliminado exitosamente', 'success')
    else:
        flash('Error al eliminar el usuario', 'error')

    return redirect(url_for('user_blueprint.list_users'))
