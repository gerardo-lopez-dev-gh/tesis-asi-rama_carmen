from flask import Blueprint, request, redirect, url_for, render_template, flash
from src.services.TratamientosAplicadosService import TratamientosAplicadosService
from src.services.AnimalService import AnimalService
from src.services.TratamientosService import TratamientosService
from src.services.AuthService import AuthService
from flask import jsonify
from src.utils.Logger import Logger

tratamiento_aplicado_blueprint = Blueprint('tratamiento_aplicado_blueprint', __name__)


@tratamiento_aplicado_blueprint.route('/list', methods=['GET'])
@AuthService.login_required
def list_tratamientos_aplicados():
    tratamientos = TratamientosAplicadosService.get_all_trata_aplicados()
    return render_template('tratamientosaplicados/list.html', tratamientos=tratamientos)


@tratamiento_aplicado_blueprint.route('/view', methods=['GET'])
@AuthService.login_required
def view_tratamiento_aplicado():
    filter_value = request.args.get('filter_value', '')
    filter_type = request.args.get('filter_type', 'id')

    if filter_value.strip() == "":
        if 'filter_value' in request.args:
            flash('Debes ingresar un valor de búsqueda', 'error')
        return render_template('tratamientosaplicados/view.html')

    if filter_type == 'id':
        tratamientos = TratamientosAplicadosService.get_trata_aplicado_by_id(filter_value)
    else:
        flash('Tipo de filtro no válido', 'error')
        return redirect(url_for('tratamiento_aplicado_blueprint.list_tratamientos_aplicados'))

    if not tratamientos:
        flash('Tratamiento aplicado no encontrado', 'error')
        return render_template('tratamientosaplicados/view.html')

    if isinstance(tratamientos, dict):
        tratamientos = [tratamientos]

    return render_template('tratamientosaplicados/view.html', tratamientos=tratamientos)


@tratamiento_aplicado_blueprint.route('/new', methods=['GET', 'POST'])
@AuthService.login_required
def new_tratamiento_aplicado_form():
    if request.method == 'POST':
        data = request.form
        id_tratamiento = data.get('id_tratamiento')
        id_animal = data.get('id_animal')
        descripcion = data.get('descripcion').upper()
        fecha_inicio = data.get('fecha_inicio')
        fecha_fin = data.get('fecha_fin')
        resultado = data.get('resultado').upper()

        if not id_tratamiento or not id_animal or not descripcion or not fecha_inicio or not fecha_fin:
            flash('Faltan datos obligatorios ', 'error')
            return redirect(url_for('tratamiento_aplicado_blueprint.new_tratamiento_aplicado_form'))

        id_tratamiento_apli = TratamientosAplicadosService.create_trata_aplicado(
            id_tratamiento=id_tratamiento,
            id_animal=id_animal,
            descripcion=descripcion,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            resultado=resultado
        )

        if id_tratamiento_apli:
            flash('Tratamiento aplicado creado exitosamente', 'success')
            return redirect(url_for('tratamiento_aplicado_blueprint.view_tratamiento_aplicado', id_tratamiento_apli=id_tratamiento_apli))
        else:
            flash('Error al crear el tratamiento a aplicar', 'error')
            return render_template('tratamientosaplicados/new.html')

    return render_template('tratamientosaplicados/new.html')


@tratamiento_aplicado_blueprint.route('/edit', methods=['GET', 'POST'])
@AuthService.login_required
def edit_tratamiento_aplicado_form():
    if request.method == 'POST':
        id_tratamiento_apli = request.form.get('id_tratamiento_apli')

        if not id_tratamiento_apli:
            flash('Debe proporcionar un ID de tratamiento aplicado', 'error')
            return redirect(url_for('tratamiento_aplicado_blueprint.edit_tratamiento_aplicado_form'))

        tratamiento = TratamientosAplicadosService.get_trata_aplicado_by_id(id_tratamiento_apli)

        if isinstance(tratamiento, list):
            tratamiento = tratamiento[0] if tratamiento else None

        if not tratamiento:
            flash('Tratamiento aplicado no encontrado', 'error')
            return redirect(url_for('tratamiento_aplicado_blueprint.edit_tratamiento_aplicado_form'))

        return render_template('tratamientosaplicados/edit.html', tratamiento=tratamiento)

    return render_template('tratamientosaplicados/edit.html')


@tratamiento_aplicado_blueprint.route('/update/<int:id_tratamiento_apli>', methods=['POST'])
@AuthService.login_required
def update_tratamiento_aplicado(id_tratamiento_apli):
    data = request.form
    id_tratamiento = data.get('id_tratamiento')
    id_animal = data.get('id_animal')
    descripcion = data.get('descripcion').upper()
    fecha_inicio = data.get('fecha_inicio')
    fecha_fin = data.get('fecha_fin')
    resultado = data.get('resultado').upper()

    if not id_tratamiento or not id_animal or not descripcion or not fecha_inicio or not fecha_fin:
        flash('Faltan datos obligatorios', 'error')
        return redirect(url_for('tratamiento_aplicado_blueprint.edit_tratamiento_aplicado_form', id_tratamiento_apli=id_tratamiento_apli))

    success = TratamientosAplicadosService.update_trata_aplicado(
        id_tratamiento_apli=id_tratamiento_apli,
        id_tratamiento=id_tratamiento,
        id_animal=id_animal,
        descripcion=descripcion,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        resultado=resultado
    )

    if success:
        flash('Tratamiento aplicado actualizado exitosamente', 'success')
        return redirect(url_for('tratamiento_aplicado_blueprint.edit_tratamiento_aplicado_form', id_tratamiento_apli=id_tratamiento_apli))
    else:
        flash('Error al actualizar el tratamiento aplicado', 'error')
        return redirect(url_for('tratamiento_aplicado_blueprint.edit_tratamiento_aplicado_form', id_tratamiento_apli=id_tratamiento_apli))


@tratamiento_aplicado_blueprint.route('/get_animal_info/<int:animal_id>', methods=['GET'])
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


@tratamiento_aplicado_blueprint.route('/get_tratamiento_info/<int:tratamiento_id>', methods=['GET'])
@AuthService.login_required
def get_tratamiento_info(tratamiento_id):
    try:
        tratamiento = TratamientosService.get_tratamiento_by_id(tratamiento_id)
        if tratamiento and len(tratamiento) > 0:
            tratamiento_data = tratamiento[0]
            return jsonify({
                'success': True,
                'descripcion': tratamiento_data['descripcion'],
                'duracion': tratamiento_data['duracion']
            })
        else:
            return jsonify({'success': False, 'message': 'Tratamiento no encontrado'}), 404
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        return jsonify({'success': False, 'message': 'Error al obtener información del tratamiento'}), 500