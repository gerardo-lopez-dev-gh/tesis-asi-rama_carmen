from flask import Blueprint, request, redirect, url_for, render_template, flash
from src.services.DietaService import DietaService
from src.services.AnimalService import AnimalService
from src.services.TablaService import TablaService
from src.services.AuthService import AuthService
from flask import jsonify
from src.utils.Logger import Logger

dieta_blueprint = Blueprint('dieta_blueprint', __name__)


@dieta_blueprint.route('/list', methods=['GET'])
@AuthService.login_required
def list_dietas():
    dietas = DietaService.get_all_dietas()
    return render_template('dieta/list.html', dietas=dietas)


@dieta_blueprint.route('/view', methods=['GET', 'POST'])
@AuthService.login_required
def view_dieta():
    filter_value = request.args.get('filter_value', '')
    filter_type = request.args.get('filter_type', 'id')

    if filter_value.strip() == "":
        if 'filter_value' in request.args:
            flash('Debes ingresar un valor de búsqueda', 'error')
        return render_template('dieta/view.html')

    if filter_type == 'id':
        dietas = DietaService.get_dieta_by_id(filter_value)
    else:
        flash('Tipo de filtro no válido', 'error')
        return redirect(url_for('dieta_blueprint.list_dietas'))

    if not dietas:
        flash('Animal no encontrado', 'error')
        return render_template('dieta/view.html')

    if isinstance(dietas, dict):
        dietas = [dietas]

    return render_template('dieta/view.html', dietas=dietas)


@dieta_blueprint.route('/new', methods=['GET', 'POST'])
def new_dieta_form():
    tipo_dieta = TablaService.get_ftabla_by_id(8)
    if request.method == 'POST':
        data = request.form
        id_animal = data.get('id_animal')
        tipo_tabla_tipo_dieta = 8
        codigo_tabla_tipo_dieta = data.get('codigo_tabla_tipo_dieta')
        descripcion = data.get('descripcion').upper()
        fecha_inicio = data.get('fecha_inicio')
        fecha_fin = data.get('fecha_fin')

        if not id_animal or not codigo_tabla_tipo_dieta or not descripcion or not fecha_inicio or not fecha_fin:
            flash('Faltan datos obligatorios', 'error')
            return redirect(url_for('dieta_blueprint.new_dieta_form'))

        id_dieta = DietaService.create_dieta(
            id_animal=id_animal,
            codigo_tabla_tipo_dieta=codigo_tabla_tipo_dieta,
            descripcion=descripcion,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            tipo_tabla_tipo_dieta=tipo_tabla_tipo_dieta
        )

        if id_dieta:
            flash('Dieta creada exitosamente', 'success')
            return redirect(url_for('dieta_blueprint.view_dieta', id_dieta=id_dieta))
        else:
            flash('Error al crear la dieta', 'error')
            return render_template('dieta/new.html', dieta=None, tipo_dieta=tipo_dieta)

    return render_template('dieta/new.html', dieta=None, tipo_dieta=tipo_dieta)


@dieta_blueprint.route('/edit', methods=['GET', 'POST'])
@AuthService.login_required
def edit_dieta_form():
    tipo_dieta = TablaService.get_ftabla_by_id(8)
    if request.method == 'POST':
        id_dieta = request.form.get('id_dieta')
        if not id_dieta:
            flash('Debe proporcionar un ID de dieta', 'error')
            return redirect(url_for('dieta_blueprint.edit_dieta_form'))

        dieta = DietaService.get_dieta_by_id(id_dieta)

        if isinstance(dieta, list):
            dieta = dieta[0] if dieta else None

        if not dieta:
            flash('Dieta no encontrada', 'error')
            return redirect(url_for('dieta_blueprint.edit_dieta_form'))

        return render_template('dieta/edit.html', dieta=dieta, tipo_dieta=tipo_dieta)

    return render_template('dieta/edit.html', dieta=None, tipo_dieta=tipo_dieta)


@dieta_blueprint.route('/update/<int:id_dieta>', methods=['POST'])
@AuthService.login_required
def update_dieta(id_dieta):
    data = request.form
    id_animal = data.get('id_animal')
    tipo_tabla_tipo_dieta = 8
    codigo_tabla_tipo_dieta = data.get('codigo_tabla_tipo_dieta')
    descripcion = data.get('descripcion').upper()
    fecha_inicio = data.get('fecha_inicio')
    fecha_fin = data.get('fecha_fin')

    if not codigo_tabla_tipo_dieta or not descripcion or not fecha_inicio or not fecha_fin:
        flash('Faltan datos obligatorios', 'error')
        return redirect(url_for('dieta_blueprint.edit_dieta_form', id_dieta=id_dieta))

    success = DietaService.update_dieta(
        id_dieta=id_dieta,
        id_animal=id_animal,
        codigo_tabla_tipo_dieta=codigo_tabla_tipo_dieta,
        descripcion=descripcion,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        tipo_tabla_tipo_dieta=tipo_tabla_tipo_dieta
    )

    if success:
        flash('Dieta actualizada exitosamente', 'success')
        return redirect(url_for('dieta_blueprint.view_dieta', id_dieta=id_dieta))
    else:
        flash('Error al actualizar la dieta', 'error')
        return redirect(url_for('dieta_blueprint.edit_dieta_form', dieta=None, id_dieta=id_dieta))


@dieta_blueprint.route('/delete/<int:id_dieta>', methods=['POST'])
@AuthService.login_required
def delete_dieta(id_dieta):
    success = DietaService.delete_dieta(id_dieta)
    if success:
        flash('Dieta eliminada exitosamente', 'success')
    else:
        flash('Error al eliminar la dieta', 'error')
    return redirect(url_for('dieta_blueprint.list_dietas'))


@dieta_blueprint.route('/get_animal_info/<int:animal_id>', methods=['GET'])
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
