from flask import Blueprint, request, redirect, url_for, render_template, flash
from src.services.UsuariosRolesService import UsuariosRolesService
from src.services.AuthService import AuthService


usuariosrol_blueprint = Blueprint('usuariosrol_blueprint', __name__)


@usuariosrol_blueprint.route('/list', methods=['GET'])
@AuthService.login_required
def list_usuarios_roles():
    usuarios_roles = UsuariosRolesService.get_all_usuarios_roles()
    return render_template('usuariosroles/list.html', usuarios_roles=usuarios_roles)


@usuariosrol_blueprint.route('/view', methods=['GET'])
@AuthService.login_required
def view_usuario_rol():
    filter_value = request.args.get('filter_value', '')
    filter_type = request.args.get('filter_type', 'id')

    if filter_value.strip() == "":
        if 'filter_value' in request.args:
            flash('Debes ingresar un valor de búsqueda', 'error')
        return render_template('usuariosroles/view.html')

    if filter_type == 'id':
        usuarios_roles = UsuariosRolesService.get_usuario_rol_by_id(filter_value)
    else:
        flash('Tipo de filtro no válido', 'error')
        return redirect(url_for('usuariosrol_blueprint.list_usuarios_roles'))

    if not usuarios_roles:
        flash('Rol no encontrado', 'error')
        return render_template('usuariosroles/view.html')

    if isinstance(usuarios_roles, dict):
        usuarios_roles = [usuarios_roles]

    return render_template('usuariosroles/view.html', usuarios_roles=usuarios_roles)


@usuariosrol_blueprint.route('/new', methods=['GET', 'POST'])
@AuthService.login_required
def new_usuario_rol_form():
    if request.method == 'POST':
        data = request.form
        id_rol = data.get('id_rol')
        id_usuario = data.get('id_usuario')

        if not id_rol or not id_usuario:
            flash('Faltan datos obligatorios ', 'error')
            return redirect(url_for('usuariosrol_blueprint.new_usuario_rol_form'))

        id_rol_usuario = UsuariosRolesService.create_usuario_rol(
            id_rol=id_rol,
            id_usuario=id_usuario
        )

        if id_rol_usuario:
            flash('Rol creado exitosamente', 'success')
            return redirect(url_for('usuariosrol_blueprint.view_usuario_rol', id_rol_usuario=id_rol_usuario))
        else:
            flash('Error al crear el rol', 'error')
            return render_template('usuariosroles/new.html')

    return render_template('usuariosroles/new.html')


@usuariosrol_blueprint.route('/edit', methods=['GET', 'POST'])
@AuthService.login_required
def edit_usuario_rol_form():
    if request.method == 'POST':
        id_rol_usuario = request.form.get('id_rol_usuario')

        if not id_rol_usuario:
            flash('Debe proporcionar un ID de rol', 'error')
            return redirect(url_for('usuariosrol_blueprint.edit_usuario_rol_form'))

        roles_usuarios = UsuariosRolesService.get_usuario_rol_by_id(id_rol_usuario)

        if isinstance(roles_usuarios, list):
            roles_usuarios = roles_usuarios[0] if roles_usuarios else None

        if not roles_usuarios:
            flash('Rol no encontrado', 'error')
            return redirect(url_for('usuariosrol_blueprint.edit_usuario_rol_form'))

        return render_template('usuariosroles/edit.html', roles_usuarios=roles_usuarios)

    return render_template('usuariosroles/edit.html')


'''@usuariosrol_blueprint.route('/update/<int:id_rol_usuario>', methods=['POST'])
@AuthService.login_required
def update_usuario_rol(id_rol_usuario):
    data = request.form
    id_rol = data.get('id_rol')
    id_usuario = data.get('id_usuario')

    if not id_rol or not id_usuario:
        flash('Faltan datos obligatorios', 'error')
        return redirect(url_for('usuariosrol_blueprint.edit_usuario_rol_form', id_rol_usuario=id_rol_usuario))

    success = UsuariosRolesService.update_historial(
        id_usu_rol=id_rol_perm,
        id_rol=id_rol,
        id_usuario=id_usuario
    )

    if success:
        flash('Rol actualizado exitosamente', 'success')
        return redirect(url_for('usuariosrol_blueprint.edit_usuario_rol_form', id_usu_rol=id_usu_rol))
    else:
        flash('Error al actualizar el rol', 'error')
        return redirect(url_for('usuariosrol_blueprint.edit_usuario_rol_form', id_usu_rol=id_usu_rol))
'''
