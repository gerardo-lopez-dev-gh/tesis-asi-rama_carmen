from flask import Blueprint, request, redirect, url_for, render_template, flash
from src.services.MedidasPreventivasService import MedidasPreventivasService
from src.services.AnimalService import AnimalService
from src.services.TablaService import TablaService
from src.services.AuthService import AuthService
from flask import jsonify
from src.utils.Logger import Logger


medidasprev_blueprint = Blueprint('medidasprev_blueprint', __name__)


@medidasprev_blueprint.route('/list', methods=['GET'])
@AuthService.login_required
def list_medidas_preventivas():
    medidas = MedidasPreventivasService.get_all_medidas_preventivas()
    return render_template('medidaspreventivas/list.html', medidas=medidas)


@medidasprev_blueprint.route('/view', methods=['GET'])
@AuthService.login_required
def view_medida_preventiva():
    filter_value = request.args.get('filter_value', '')
    filter_type = request.args.get('filter_type', 'id')

    if filter_value.strip() == "":
        if 'filter_value' in request.args:
            flash('Debes ingresar un valor de búsqueda', 'error')
        return render_template('medidaspreventivas/view.html')

    if filter_type == 'id':
        medidas = MedidasPreventivasService.get_medida_preventiva_by_id(filter_value)
    else:
        flash('Tipo de filtro no válido', 'error')
        return redirect(url_for('medidasprev_blueprint.list_historiales'))

    if not medidas:
        flash('Medida preventiva no encontrada', 'error')
        return render_template('medidaspreventivas/view.html')

    if isinstance(medidas, dict):
        medidas = [medidas]

    return render_template('medidaspreventivas/view.html', medidas=medidas)


@medidasprev_blueprint.route('/new', methods=['GET', 'POST'])
@AuthService.login_required
def new_medida_preventiva_form():
    tipos_medida = TablaService.get_ftabla_by_id(10)
    if request.method == 'POST':
        data = request.form
        id_animal = data.get('id_animal')
        tipo_tabla_tipo_medida = 10
        codigo_tabla_tipo_medida = data.get('codigo_tabla_tipo_medida')
        descripcion = data.get('descripcion').upper()
        fecha = data.get('fecha')

        if not id_animal or not codigo_tabla_tipo_medida or not descripcion or not fecha:
            flash('Faltan datos obligatorios ', 'error')
            return redirect(url_for('medidasprev_blueprint.new_medida_preventiva_form'))

        id_med_prev = MedidasPreventivasService.create_medida_preventiva(
            id_animal=id_animal,
            tipo_tabla_tipo_medida=tipo_tabla_tipo_medida,
            codigo_tabla_tipo_medida=codigo_tabla_tipo_medida,
            descripcion=descripcion,
            fecha=fecha
        )

        if id_med_prev:
            flash('Medida preventiva creada exitosamente', 'success')
            return redirect(url_for('medidasprev_blueprint.view_medida_preventiva', id_med_prev=id_med_prev, tipos_medida=tipos_medida))
        else:
            flash('Error al crear al medida preventiva', 'error')
            return render_template('medidaspreventivas/new.html', tipos_medida=tipos_medida)

    return render_template('medidaspreventivas/new.html', tipos_medida=tipos_medida)


@medidasprev_blueprint.route('/edit', methods=['GET', 'POST'])
@AuthService.login_required
def edit_medida_preventiva_form():
    tipos_medida = TablaService.get_ftabla_by_id(10)
    if request.method == 'POST':
        id_med_prev = request.form.get('id_med_prev')

        if not id_med_prev:
            flash('Debe proporcionar un ID de medida preventiva', 'error')
            return redirect(url_for('medidasprev_blueprint.edit_medida_preventiva_form'))

        medidas = MedidasPreventivasService.get_medida_preventiva_by_id(id_med_prev)

        if isinstance(medidas, list):
            medidas = medidas[0] if medidas else None

        if not medidas:
            flash('Medida preventiva no encontrada', 'error')
            return redirect(url_for('medidasprev_blueprint.edit_medida_preventiva_form'))

        return render_template('medidaspreventivas/edit.html', medidas=medidas, tipos_medida=tipos_medida)

    return render_template('medidaspreventivas/edit.html', medidas=None, tipos_medida=tipos_medida)


@medidasprev_blueprint.route('/update/<int:id_med_prev>', methods=['POST'])
@AuthService.login_required
def update_medida_preventiva(id_med_prev):
    data = request.form
    id_animal = data.get('id_animal')
    tipo_tabla_tipo_medida = 10
    codigo_tabla_tipo_medida = data.get('codigo_tabla_tipo_medida')
    descripcion = data.get('descripcion').upper()
    fecha = data.get('fecha')

    if not id_animal or not codigo_tabla_tipo_medida or not descripcion or not fecha:
        flash('Faltan datos obligatorios', 'error')
        return redirect(url_for('medidasprev_blueprint.edit_medida_preventiva_form', id_med_prev=id_med_prev))

    success = MedidasPreventivasService.update_medida_preventiva(
        id_medida=id_med_prev,
        id_animal=id_animal,
        tipo_tabla_tipo_medida=tipo_tabla_tipo_medida,
        codigo_tabla_tipo_medida=codigo_tabla_tipo_medida,
        descripcion=descripcion,
        fecha=fecha
    )

    if success:
        flash('Medida preventiva actualizada exitosamente', 'success')
        return redirect(url_for('medidasprev_blueprint.edit_medida_preventiva_form', id_med_prev=id_med_prev))
    else:
        flash('Error al actualizar al medida preventiva', 'error')
        return redirect(url_for('medidasprev_blueprint.edit_medida_preventiva_form', id_med_prev=id_med_prev))


@medidasprev_blueprint.route('/get_animal_info/<int:animal_id>', methods=['GET'])
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
