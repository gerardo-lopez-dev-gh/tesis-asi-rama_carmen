from flask import Blueprint, request, redirect, url_for, render_template, flash
from src.services.HistorialMedicoService import HistorialMedicoService
from src.services.AnimalService import AnimalService
from src.services.AuthService import AuthService
from flask import jsonify
from src.utils.Logger import Logger


historialmed_blueprint = Blueprint('historialmed_blueprint', __name__)


@historialmed_blueprint.route('/list', methods=['GET'])
@AuthService.login_required
def list_historiales():
    historiales = HistorialMedicoService.get_all_historiales()
    return render_template('historialmedico/list.html', historiales=historiales)


@historialmed_blueprint.route('/view', methods=['GET'])
@AuthService.login_required
def view_historial():
    filter_value = request.args.get('filter_value', '')
    filter_type = request.args.get('filter_type', 'id')

    if filter_value.strip() == "":
        if 'filter_value' in request.args:
            flash('Debes ingresar un valor de búsqueda', 'error')
        return render_template('historialmedico/view.html')

    if filter_type == 'id':
        historiales = HistorialMedicoService.get_historial_by_id(filter_value)
    else:
        flash('Tipo de filtro no válido', 'error')
        return redirect(url_for('historialmed_blueprint.list_historiales'))

    if not historiales:
        flash('Historial médico no encontrado', 'error')
        return render_template('historialmedico/view.html')

    if isinstance(historiales, dict):
        historiales = [historiales]

    return render_template('historialmedico/view.html', historiales=historiales)


@historialmed_blueprint.route('/new', methods=['GET', 'POST'])
@AuthService.login_required
def new_historial_form():
    if request.method == 'POST':
        data = request.form
        id_animal = data.get('id_animal')
        descripcion = data.get('descripcion').upper()
        fecha = data.get('fecha')

        if not id_animal or not descripcion or not fecha:
            flash('Faltan datos obligatorios ', 'error')
            return redirect(url_for('historialmed_blueprint.new_historial_form'))

        id_historial = HistorialMedicoService.create_historial(
            id_animal=id_animal,
            descripcion=descripcion,
            fecha=fecha
        )

        if id_historial:
            flash('Historial médico creado exitosamente', 'success')
            return redirect(url_for('historialmed_blueprint.view_historial', id_historial=id_historial))
        else:
            flash('Error al crear el historial médico', 'error')
            return render_template('historialmedico/new.html')

    return render_template('historialmedico/new.html')


@historialmed_blueprint.route('/edit', methods=['GET', 'POST'])
@AuthService.login_required
def edit_historial_form():
    if request.method == 'POST':
        id_historial = request.form.get('id_historial')

        if not id_historial:
            flash('Debe proporcionar un ID de historial médico', 'error')
            return redirect(url_for('historialmed_blueprint.edit_historial_form'))

        historiales = HistorialMedicoService.get_historial_by_id(id_historial)

        if isinstance(historiales, list):
            historiales = historiales[0] if historiales else None

        if not historiales:
            flash('Historial médico no encontrado', 'error')
            return redirect(url_for('historialmed_blueprint.edit_historial_form'))

        return render_template('historialmedico/edit.html', historiales=historiales)

    return render_template('historialmedico/edit.html')


@historialmed_blueprint.route('/update/<int:id_historial>', methods=['POST'])
@AuthService.login_required
def update_historial(id_historial):
    data = request.form
    id_animal = data.get('id_animal')
    descripcion = data.get('descripcion').upper()
    fecha = data.get('fecha')

    if not id_animal or not descripcion or not fecha:
        flash('Faltan datos obligatorios', 'error')
        return redirect(url_for('historialmed_blueprint.edit_historial_form', id_historial=id_historial))

    success = HistorialMedicoService.update_historial(
        id_historial=id_historial,
        id_animal=id_animal,
        descripcion=descripcion,
        fecha=fecha
    )

    if success:
        flash('Historial médico actualizado exitosamente', 'success')
        return redirect(url_for('historialmed_blueprint.edit_historial_form', id_historial=id_historial))
    else:
        flash('Error al actualizar el historial médico', 'error')
        return redirect(url_for('historialmed_blueprint.edit_historial_form', id_historial=id_historial))


@historialmed_blueprint.route('/get_animal_info/<int:animal_id>', methods=['GET'])
@AuthService.login_required
def get_animal_info(animal_id):
    try:
        animal = AnimalService.get_animal_by_id(animal_id)
        if animal and len(animal) > 0:
            animal_data = animal[0]
            return jsonify({
                'success': True,
                'tipo_tabla_tipo_animal': animal_data['tipo_tabla_tipo_animal'],
                'codigo_tabla_tipo_animal': animal_data['codigo_tabla_tipo_animal'],
                'fecha_nacimiento': animal_data['fecha_nacimiento'],
                'peso': animal_data['peso'],
                'tipo_tabla_estado_salud': animal_data['tipo_tabla_estado_salud'],
                'codigo_tabla_estado_salud': animal_data['codigo_tabla_estado_salud'],
                'tipo_tabla_estado_registro': animal_data['tipo_tabla_estado_registro'],
                'codigo_tabla_estado_registro': animal_data['codigo_tabla_estado_registro'],
                'estado_salud': animal_data['estado_salud'],
                'tipo_animal': animal_data['tipo_animal'],
                'estado_registro': animal_data['estado_registro']
            })
        else:
            return jsonify({'success': False, 'message': 'Animal no encontrado'}), 404
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        return jsonify({'success': False, 'message': 'Error al obtener información del animal'}), 500
