from flask import Blueprint, request, redirect, url_for, render_template, flash
from src.services.RolesService import RolesService
from src.services.AuthService import AuthService


roles_blueprint = Blueprint('roles_blueprint', __name__)


@roles_blueprint.route('/list', methods=['GET'])
@AuthService.login_required
def list_roles():
    roles = RolesService.get_all_roles()
    return render_template('roles/list.html', roles=roles)


@roles_blueprint.route('/view', methods=['GET'])
@AuthService.login_required
def view_rol():
    filter_value = request.args.get('filter_value', '')
    filter_type = request.args.get('filter_type', 'id')

    if filter_value.strip() == "":
        if 'filter_value' in request.args:
            flash('Debes ingresar un valor de búsqueda', 'error')
        return render_template('roles/view.html')

    if filter_type == 'id':
        roles = RolesService.get_rol_by_id(filter_value)
    else:
        flash('Tipo de filtro no válido', 'error')
        return redirect(url_for('roles_blueprint.list_roles'))

    if not roles:
        flash('Rol no encontrado', 'error')
        return render_template('roles/view.html')

    if isinstance(roles, dict):
        roles = [roles]

    return render_template('roles/view.html', roles=roles)


@roles_blueprint.route('/new', methods=['GET', 'POST'])
@AuthService.login_required
def new_rol_form():
    if request.method == 'POST':
        data = request.form
        nombre_rol = data.get('nombre_rol').upper()
        descripcion = data.get('descripcion').upper()

        if not nombre_rol or not descripcion:
            flash('Faltan datos obligatorios ', 'error')
            return redirect(url_for('roles_blueprint.new_rol_form'))

        id_rol = RolesService.create_rol(
            nombre_rol=nombre_rol,
            descripcion=descripcion
        )

        if id_rol:
            flash('Rol creado exitosamente', 'success')
            return redirect(url_for('roles_blueprint.view_rol', id_rol=id_rol))
        else:
            flash('Error al crear el rol', 'error')
            return render_template('roles/new.html')

    return render_template('roles/new.html')


@roles_blueprint.route('/edit', methods=['GET', 'POST'])
@AuthService.login_required
def edit_rol_form():
    if request.method == 'POST':
        id_rol = request.form.get('id_rol')
        
        if not id_rol:
            flash('Debe proporcionar un ID de rol', 'error')
            return redirect(url_for('roles_blueprint.edit_rol_form'))

        roles = RolesService.get_rol_by_id(id_rol)

        if isinstance(roles, list):
            roles = roles[0] if roles else None

        if not roles:
            flash('Rol no encontrado', 'error')
            return redirect(url_for('roles_blueprint.edit_rol_form'))

        return render_template('roles/edit.html', roles=roles)

    return render_template('roles/edit.html')


@roles_blueprint.route('/update/<int:id_rol>', methods=['POST'])
@AuthService.login_required
def update_rol(id_rol):
    data = request.form
    nombre_rol = data.get('nombre_rol').upper()
    descripcion = data.get('descripcion').upper()

    if not nombre_rol or not descripcion:
        flash('Faltan datos obligatorios', 'error')
        return redirect(url_for('roles_blueprint.edit_rol_form', id_rol=id_rol))

    success = RolesService.update_rol(
        id_rol=id_rol,
        nombre_rol=nombre_rol,
        descripcion=descripcion
    )

    if success:
        flash('Rol actualizado exitosamente', 'success')
        return redirect(url_for('roles_blueprint.view_rol', id_rol=id_rol))
    else:
        flash('Error al actualizar el rol', 'error')
        return redirect(url_for('roles_blueprint.edit_rol_form', id_rol=id_rol))
