from flask import Blueprint, request, redirect, url_for, render_template, flash
from src.services.TratamientosService import TratamientosService
from src.services.AuthService import AuthService


tratamiento_blueprint = Blueprint('tratamiento_blueprint', __name__)


@tratamiento_blueprint.route('/list', methods=['GET'])
@AuthService.login_required
def list_tratamientos():
    tratamientos = TratamientosService.get_all_tratamientos()
    return render_template('tratamientos/list.html', tratamientos=tratamientos)


@tratamiento_blueprint.route('/view', methods=['GET'])
@AuthService.login_required
def view_tratamiento():
    filter_value = request.args.get('filter_value', '')
    filter_type = request.args.get('filter_type', 'id')

    if filter_value.strip() == "":
        if 'filter_value' in request.args:
            flash('Debes ingresar un valor de búsqueda', 'error')
        return render_template('tratamientos/view.html')

    if filter_type == 'id':
        tratamientos = TratamientosService.get_tratamiento_by_id(filter_value)
    else:
        flash('Tipo de filtro no válido', 'error')
        return redirect(url_for('tratamiento_blueprint.list_tratamientos'))

    if not tratamientos:
        flash('Tratamiento no encontrado', 'error')
        return render_template('tratamientos/view.html')

    if isinstance(tratamientos, dict):
        tratamientos = [tratamientos]

    return render_template('tratamientos/view.html', tratamientos=tratamientos)


@tratamiento_blueprint.route('/new', methods=['GET', 'POST'])
@AuthService.login_required
def new_tratamiento_form():
    if request.method == 'POST':
        data = request.form
        descripcion = data.get('descripcion').upper()
        duracion = data.get('duracion')

        if not descripcion or not duracion:
            flash('Faltan datos obligatorios ', 'error')
            return redirect(url_for('tratamiento_blueprint.new_tratamiento_form'))

        id_tratamiento = TratamientosService.create_tratamiento(
            descripcion=descripcion,
            duracion=duracion
        )

        if id_tratamiento:
            flash('Tratamiento creado exitosamente', 'success')
            return redirect(url_for('tratamiento_blueprint.view_tratamiento', id_tratamiento=id_tratamiento))
        else:
            flash('Error al crear el tratamiento', 'error')
            return render_template('tratamientos/new.html')

    return render_template('tratamientos/new.html')


@tratamiento_blueprint.route('/edit', methods=['GET', 'POST'])
@AuthService.login_required
def edit_tratamiento_form():
    if request.method == 'POST':
        id_tratamiento = request.form.get('id_tratamiento')

        if not id_tratamiento:
            flash('Debe proporcionar un ID de tratamiento', 'error')
            return redirect(url_for('tratamiento_blueprint.edit_tratamiento_form'))

        tratamiento = TratamientosService.get_tratamiento_by_id(id_tratamiento)

        if isinstance(tratamiento, list):
            tratamiento = tratamiento[0] if tratamiento else None

        if not tratamiento:
            flash('Tratamiento no encontrado', 'error')
            return redirect(url_for('tratamiento_blueprint.edit_tratamiento_form'))

        return render_template('tratamientos/edit.html', tratamiento=tratamiento)

    return render_template('tratamientos/edit.html')


@tratamiento_blueprint.route('/update/<int:id_tratamiento>', methods=['POST'])
@AuthService.login_required
def update_tratamiento(id_tratamiento):
    data = request.form
    descripcion = data.get('descripción').upper()
    duracion = data.get('duracion')

    if not descripcion or not duracion:
        flash('Faltan datos obligatorios', 'error')
        return redirect(url_for('tratamiento_blueprint.edit_tratamiento_form', id_tratamiento=id_tratamiento))

    success = TratamientosService.update_tratamiento(
        id_tratamiento=id_tratamiento,
        descripcion=descripcion,
        duracion=duracion
    )

    if success:
        flash('Tratamiento actualizado exitosamente', 'success')
        return redirect(url_for('tratamiento_blueprint.edit_tratamiento_form', id_tratamiento=id_tratamiento))
    else:
        flash('Error al actualizar el tratamiento', 'error')
        return redirect(url_for('tratamiento_blueprint.edit_tratamiento_form', id_tratamiento=id_tratamiento))
