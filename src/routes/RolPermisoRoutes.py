from flask import Blueprint, request, redirect, url_for, render_template, flash
from src.services.RolPermisoService import RolesPermisosService
from src.services.AuthService import AuthService


rolpermiso_blueprint = Blueprint('rolpermiso_blueprint', __name__)


@rolpermiso_blueprint.route('/list', methods=['GET'])
@AuthService.login_required
def list_roles_permisos():
    roles_permisos = RolesPermisosService.get_all_roles_permisos()
    return render_template('rolespermisos/list.html', roles_permisos=roles_permisos)


@rolpermiso_blueprint.route('/view', methods=['GET'])
@AuthService.login_required
def view_rol_permiso():
    filter_value = request.args.get('filter_value', '')
    filter_type = request.args.get('filter_type', 'id')

    if filter_value.strip() == "":
        if 'filter_value' in request.args:
            flash('Debes ingresar un valor de búsqueda', 'error')
        return render_template('rolespermisos/view.html')

    if filter_type == 'id':
        roles_permisos = RolesPermisosService.get_rol_permiso_by_id(filter_value)
    else:
        flash('Tipo de filtro no válido', 'error')
        return redirect(url_for('rolpermiso_blueprint.list_roles_permisos'))

    if not roles_permisos:
        flash('Rol no encontrado', 'error')
        return render_template('rolespermisos/view.html')

    if isinstance(roles_permisos, dict):
        roles_permisos = [roles_permisos]

    return render_template('rolespermisos/view.html', roles_permisos=roles_permisos)


@rolpermiso_blueprint.route('/new', methods=['GET', 'POST'])
@AuthService.login_required
def new_rol_permiso_form():
    if request.method == 'POST':
        data = request.form
        id_rol = data.get('id_rol')
        id_permiso = data.get('id_permiso')

        if not id_rol or not id_permiso:
            flash('Faltan datos obligatorios ', 'error')
            return redirect(url_for('rolpermiso_blueprint.new_rol_permiso_form'))

        id_rol_permiso = RolesPermisosService.create_rol_permiso(
            id_rol=id_rol,
            id_permiso=id_permiso
        )

        if id_rol_permiso:
            flash('Rol creado exitosamente', 'success')
            return redirect(url_for('rolpermiso_blueprint.view_rol_permiso', id_rol_permiso=id_rol_permiso))
        else:
            flash('Error al crear el rol', 'error')
            return render_template('rolespermisos/new.html')

    return render_template('rolespermisos/new.html')


@rolpermiso_blueprint.route('/edit', methods=['GET', 'POST'])
@AuthService.login_required
def edit_rol_permiso_form():
    if request.method == 'POST':
        id_rol_permiso = request.form.get('id_rol_permiso')

        if not id_rol_permiso:
            flash('Debe proporcionar un ID de rol', 'error')
            return redirect(url_for('rolpermiso_blueprint.edit_rol_permiso_form'))

        roles_permisos = RolesPermisosService.get_rol_permiso_by_id(id_rol_permiso)

        if isinstance(roles_permisos, list):
            roles_permisos = roles_permisos[0] if roles_permisos else None

        if not roles_permisos:
            flash('Rol no encontrado', 'error')
            return redirect(url_for('rolpermiso_blueprint.edit_rol_permiso_form'))

        return render_template('rolespermisos/edit.html', roles_permisos=roles_permisos)

    return render_template('rolespermisos/edit.html')


'''@rolpermiso_blueprint.route('/update/<int:id_rol_permiso>', methods=['POST'])
@AuthService.login_required
def update_historial(id_rol_permiso):
    data = request.form
    id_rol = data.get('id_rol')
    id_permiso = data.get('id_permiso')

    if not id_rol or not id_permiso:
        flash('Faltan datos obligatorios', 'error')
        return redirect(url_for('rolpermiso_blueprint.edit_rol_permiso_form', id_rol_permiso=id_rol_permiso))

    success = RolesPermisosService.update_historial(
        id_rol_permiso=id_rol_permiso,
        id_rol=id_rol,
        id_permiso=id_permiso
    )

    if success:
        flash('Rol actualizado exitosamente', 'success')
        return redirect(url_for('rolpermiso_blueprint.edit_rol_permiso_form', id_rol_permiso=id_rol_permiso))
    else:
        flash('Error al actualizar el rol', 'error')
        return redirect(url_for('rolpermiso_blueprint.edit_rol_permiso_form', id_rol_permiso=id_rol_permiso))
'''
