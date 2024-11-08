from flask import Blueprint, request, redirect, url_for, render_template, flash
from src.services.GeneralService import GeneralService
from src.services.UserService import UserService
from src.services.TablaService import TablaService
from src.services.AuthService import AuthService

general_blueprint = Blueprint('general_blueprint', __name__)


@general_blueprint.route('/list', methods=['GET'])
@AuthService.login_required
def list_persons():
    persona = GeneralService.get_all_persons()
    return render_template('general/list.html', personas=persona)


@general_blueprint.route('/view', methods=['GET'])
@AuthService.login_required
def view_person():
    filter_value = request.args.get('filter_value', '')
    filter_type = request.args.get('filter_type', 'id')

    if filter_value.strip() == "":
        if 'filter_value' in request.args:
            flash('Debes ingresar un valor de búsqueda', 'error')
        return render_template('general/view.html')

    if filter_type == 'id':
        personas = GeneralService.get_person_by_id(filter_value)
    elif filter_type == 'nombre':
        personas = GeneralService.get_person_by_name(filter_value)
    elif filter_type == 'apellido':
        personas = GeneralService.get_person_by_lastname(filter_value)
    else:
        flash('Tipo de filtro no válido', 'error')
        return redirect(url_for('general_blueprint.list_persons'))

    if not personas:
        flash('Persona no encontrada', 'error')
        return render_template('general/view.html')

    if isinstance(personas, dict):
        personas = [personas]

    return render_template('general/view.html', personas=personas)


@general_blueprint.route('/new', methods=['GET', 'POST'])
@AuthService.login_required
def new_person_form():
    estado_civil = TablaService.get_ftabla_by_id(1)
    tipo_documento = TablaService.get_ftabla_by_id(11)
    estado_registro = TablaService.get_ftabla_by_id(13)
    tipo_registro = TablaService.get_ftabla_by_id(2)

    if request.method == 'POST':
        data = request.form
        nombre = data.get('nombre').upper()
        direccion = data.get('direccion').upper()
        telefono = data.get('telefono')
        correo_electronico = data.get('correo_electronico')
        tipo_tabla_estado_civil = 1
        codigo_tabla_estado_civil = data.get('codigo_tabla_estado_civil')
        documento = data.get('documento')
        tipo_tabla_tipo_documento = 11
        codigo_tabla_tipo_documento = data.get('codigo_tabla_tipo_documento')
        tipo_tabla_estado_registro = 13
        codigo_tabla_estado_registro = data.get('codigo_tabla_estado_registro')
        tipo_tabla_tipo_registro = 2
        codigo_tabla_tipo_registro = data.get('codigo_tabla_tipo_registro')

        registrar_usuario = data.get('radio-group')
        operador = data.get('operador')
        contrasena = data.get('contrasena')

        if not nombre or not direccion or not telefono or not correo_electronico or not documento or not codigo_tabla_tipo_documento:
            flash('Faltan datos obligatorios ', 'error')
            return redirect(url_for('general_blueprint.new_person_form'))

        id_persona = GeneralService.create_person(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            correo_electronico=correo_electronico,
            codigo_tabla_estado_civil=codigo_tabla_estado_civil,
            documento=documento,
            codigo_tabla_tipo_documento=codigo_tabla_tipo_documento,
            codigo_tabla_estado_registro=codigo_tabla_estado_registro,
            codigo_tabla_tipo_registro=codigo_tabla_tipo_registro,
            tipo_tabla_estado_civil=tipo_tabla_estado_civil,
            tipo_tabla_tipo_documento=tipo_tabla_tipo_documento,
            tipo_tabla_estado_registro=tipo_tabla_estado_registro,
            tipo_tabla_tipo_registro=tipo_tabla_tipo_registro
        )

        if registrar_usuario != "1" and registrar_usuario != "2":
            flash('Debe seleccionar una opción para registrar al usuario', 'error')

        if registrar_usuario == "1":
            id_usuario = UserService.create_user(
                id_persona=id_persona,
                operador=operador,
                contrasena=contrasena,
                codigo_tabla_estado_registro=1,
                codigo_tabla_tipo_registro=5
            )

            if id_usuario:
                flash('Usuario creado exitosamente', 'success')
                return redirect(url_for('general_blueprint.view_person', id_persona=id_persona))
            else:
                flash('Error al crear el usuario', 'error')
                return redirect(url_for('general_blueprint.new_person_form'))

        if registrar_usuario is None:
            flash('Debe seleccionar una opción para registrar al usuario', 'error')
            return render_template(
                'general/new.html',
                estado_civil=estado_civil,
                tipo_documento=tipo_documento,
                estado_registro=estado_registro,
                tipo_registro=tipo_registro,
                nombre=nombre,
                direccion=direccion,
                telefono=telefono,
                correo_electronico=correo_electronico,
                documento=documento,
                codigo_tabla_estado_civil=codigo_tabla_estado_civil,
                codigo_tabla_tipo_documento=codigo_tabla_tipo_documento,
                codigo_tabla_estado_registro=codigo_tabla_estado_registro,
                codigo_tabla_tipo_registro=codigo_tabla_tipo_registro
            )

        if id_persona:
            flash('Persona creada exitosamente', 'success')
            return redirect(url_for('general_blueprint.view_person', id_persona=id_persona))
        else:
            flash('Error al crear la persona', 'error')
            return render_template('general/new.html', estado_civil=estado_civil, tipo_documento=tipo_documento, estado_registro=estado_registro, tipo_registro=tipo_registro)

    return render_template('general/new.html', estado_civil=estado_civil, tipo_documento=tipo_documento, estado_registro=estado_registro, tipo_registro=tipo_registro)


@general_blueprint.route('/edit', methods=['GET', 'POST'])
@AuthService.login_required
def edit_person_form():
    estado_civil = TablaService.get_ftabla_by_id(1)
    tipo_documento = TablaService.get_ftabla_by_id(11)
    estado_registro = TablaService.get_ftabla_by_id(13)
    tipo_registro = TablaService.get_ftabla_by_id(2)

    if request.method == 'POST':
        id_persona = request.form.get('id_persona')

        if not id_persona:
            flash('Debe proporcionar un ID de persona', 'error')
            return redirect(url_for('general_blueprint.edit_person_form'))

        persona = GeneralService.get_person_by_id(id_persona)

        if isinstance(persona, list):
            persona = persona[0] if persona else None

        if not persona:
            flash('Persona no encontrada', 'error')
            return redirect(url_for('general_blueprint.edit_person_form'))

        return render_template('general/edit.html', persona=persona, estado_civil=estado_civil, tipo_documento=tipo_documento, estado_registro=estado_registro, tipo_registro=tipo_registro)

    return render_template('general/edit.html', estado_civil=estado_civil, tipo_documento=tipo_documento, estado_registro=estado_registro, tipo_registro=tipo_registro)


@general_blueprint.route('/update/<int:id_persona>', methods=['POST'])
@AuthService.login_required
def update_person(id_persona):
    data = request.form
    nombre = data.get('nombre').upper()
    direccion = data.get('direccion').upper()
    telefono = data.get('telefono')
    correo_electronico = data.get('correo_electronico')
    tipo_tabla_estado_civil = 1
    codigo_tabla_estado_civil = data.get('codigo_tabla_estado_civil')
    documento = data.get('documento')
    tipo_tabla_tipo_documento = 11
    codigo_tabla_tipo_documento = data.get('codigo_tabla_tipo_documento')

    if not nombre or not direccion or not telefono or not correo_electronico or not documento or not codigo_tabla_tipo_documento:
        flash('Faltan datos obligatorios', 'error')
        return redirect(url_for('general_blueprint.edit_person_form', id_persona=id_persona))

    success = GeneralService.update_person(
        id_persona=id_persona,
        nombre=nombre,
        direccion=direccion,
        telefono=telefono,
        correo_electronico=correo_electronico,
        codigo_tabla_estado_civil=codigo_tabla_estado_civil,
        documento=documento,
        codigo_tabla_tipo_documento=codigo_tabla_tipo_documento,
        tipo_tabla_estado_civil=tipo_tabla_estado_civil,
        tipo_tabla_tipo_documento=tipo_tabla_tipo_documento
    )

    if success:
        flash('Persona actualizada exitosamente', 'success')
        return redirect(url_for('general_blueprint.edit_person_form', id_persona=id_persona))
    else:
        flash('Error al actualizar la persona', 'error')
        return redirect(url_for('general_blueprint.edit_person_form', id_persona=id_persona))


@general_blueprint.route('/delete/<int:id_persona>', methods=['POST'])
@AuthService.login_required
def delete_person(id_persona):
    success = GeneralService.delete_person(id_persona)

    if success:
        flash('Persona eliminada exitosamente', 'success')
    else:
        flash('Error al eliminar la persona', 'error')

    return redirect(url_for('general_blueprint.list_persons'))
