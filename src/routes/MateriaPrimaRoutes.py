from flask import Blueprint, request, redirect, url_for, render_template, flash
from src.services.MateriaPrimaService import MateriaPrimaService
from src.services.AnimalService import AnimalService
from src.services.AuthService import AuthService
from flask import jsonify
from src.utils.Logger import Logger


materiaprima_blueprint = Blueprint('materiaprima_blueprint', __name__)


@materiaprima_blueprint.route('/list', methods=['GET'])
@AuthService.login_required
def list_materias_primas():
    materias = MateriaPrimaService.get_all_materias_prima()
    return render_template('materiaprima/list.html', materias=materias)


@materiaprima_blueprint.route('/view', methods=['GET'])
@AuthService.login_required
def view_materia_prima():
    filter_value = request.args.get('filter_value', '')
    filter_type = request.args.get('filter_type', 'id')

    if filter_value.strip() == "":
        if 'filter_value' in request.args:
            flash('Debes ingresar un valor de búsqueda', 'error')
        return render_template('materiaprima/view.html')

    if filter_type == 'id':
        materias = MateriaPrimaService.get_materia_prima_by_id(filter_value)
    else:
        flash('Tipo de filtro no válido', 'error')
        return redirect(url_for('materiaprima_blueprint.list_materias'))

    if not materias:
        flash('Materia prima no encontrada', 'error')
        return render_template('materiaprima/view.html')

    if isinstance(materias, dict):
        materias = [materias]

    return render_template('materiaprima/view.html', materias=materias)


@materiaprima_blueprint.route('/new', methods=['GET', 'POST'])
@AuthService.login_required
def new_materia_prima_form():
    if request.method == 'POST':
        data = request.form
        id_animal = data.get('id_animal')
        descripcion = data.get('descripcion').upper()
        fecha_obtencion = data.get('fecha_obtencion')
        cantidad = data.get('cantidad')

        if not id_animal or not descripcion or not fecha_obtencion or not cantidad:
            flash('Faltan datos obligatorios ', 'error')
            return redirect(url_for('materiaprima_blueprint.new_materia_prima_form'))

        id_mat_pri = MateriaPrimaService.create_materia_prima(
            id_animal=id_animal,
            descripcion=descripcion,
            fecha_obtencion=fecha_obtencion,
            cantidad=cantidad
        )

        if id_mat_pri:
            flash('Registro de materia prima creado exitosamente', 'success')
            return redirect(url_for('materiaprima_blueprint.view_materia_prima', id_mat_pri=id_mat_pri))
        else:
            flash('Error al crear el registro de materia prima', 'error')
            return render_template('materiaprima/new.html')

    return render_template('materiaprima/new.html')


@materiaprima_blueprint.route('/edit', methods=['GET', 'POST'])
@AuthService.login_required
def edit_materia_prima_form():
    if request.method == 'POST':
        id_mat_pri = request.form.get('id_mat_pri')
        if not id_mat_pri:
            flash('Debe proporcionar un ID de registro de materia prima', 'error')
            return redirect(url_for('materiaprima_blueprint.edit_materia_prima_form'))

        materias = MateriaPrimaService.get_materia_prima_by_id(id_mat_pri)

        if isinstance(materias, list):
            materias = materias[0] if materias else None

        if not materias:
            flash('Registro de materia prima no encontrado', 'error')
            return redirect(url_for('materiaprima_blueprint.edit_materia_prima_form'))

        return render_template('materiaprima/edit.html', materias=materias)

    return render_template('materiaprima/edit.html')


@materiaprima_blueprint.route('/update/<int:id_mat_pri>', methods=['POST'])
@AuthService.login_required
def update_materia_prima(id_mat_pri):
    data = request.form
    id_animal = data.get('id_animal')
    descripcion = data.get('descripcion').upper()
    fecha_obtencion = data.get('fecha_obtencion')
    cantidad = data.get('cantidad')

    if not id_animal or not descripcion or not fecha_obtencion or not cantidad:
        flash('Faltan datos obligatorios', 'error')
        return redirect(url_for('materiaprima_blueprint.edit_materia_prima_form', id_mat_pri=id_mat_pri))

    success = MateriaPrimaService.update_materia_prima(
        id_prima=id_mat_pri,
        id_animal=id_animal,
        descripcion=descripcion,
        fecha_obtencion=fecha_obtencion,
        cantidad=cantidad
    )

    if success:
        flash('Registro de materia prima actualizado exitosamente', 'success')
        return redirect(url_for('materiaprima_blueprint.view_materia_prima', id_mat_pri=id_mat_pri))
    else:
        flash('Error al actualizar el registro de materia prima', 'error')
        return redirect(url_for('materiaprima_blueprint.edit_materia_prima_form', id_mat_pri=id_mat_pri))


@materiaprima_blueprint.route('/get_animal_info/<int:animal_id>', methods=['GET'])
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
