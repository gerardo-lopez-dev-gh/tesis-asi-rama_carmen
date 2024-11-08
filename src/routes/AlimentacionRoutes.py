from flask import Blueprint, request, redirect, url_for, render_template, flash
from src.services.AlimentacionService import AlimentacionService
from src.services.DietaService import DietaService
from src.services.TablaService import TablaService
from src.services.AuthService import AuthService
from flask import jsonify
from src.utils.Logger import Logger

alimentacion_blueprint = Blueprint('alimentacion_blueprint', __name__)


@alimentacion_blueprint.route('/list', methods=['GET'])
@AuthService.login_required
def list_alimentaciones():
    alimentaciones = AlimentacionService.get_all_alimentaciones()
    return render_template('alimentacion/list.html', alimentaciones=alimentaciones)


@alimentacion_blueprint.route('/view', methods=['GET'])
@AuthService.login_required
def view_alimentacion():
    filter_value = request.args.get('filter_value', '')
    filter_type = request.args.get('filter_type', 'id')

    if filter_value.strip() == "":
        if 'filter_value' in request.args:
            flash('Debes ingresar un valor de búsqueda', 'error')
        return render_template('alimentacion/view.html')

    if filter_type == 'id':
        alimentaciones = AlimentacionService.get_alimentacion_by_id(filter_value)
    else:
        flash('Tipo de filtro no válido', 'error')
        return redirect(url_for('alimentacion_blueprint.list_alimentaciones'))

    if not alimentaciones:
        flash('Alimentacion no encontrada', 'error')
        return render_template('alimentacion/view.html')

    if isinstance(alimentaciones, dict):
        alimentaciones = [alimentaciones]

    return render_template('alimentacion/view.html', alimentaciones=alimentaciones)


@alimentacion_blueprint.route('/new', methods=['GET', 'POST'])
@AuthService.login_required
def new_alimentacion_form():
    tipos_alimento = TablaService.get_ftabla_by_id(9)
    if request.method == 'POST':
        data = request.form
        id_dieta = data.get('id_dieta')
        tipo_tabla_tipo_alimento = 9
        codigo_tabla_tipo_alimento = data.get('codigo_tabla_tipo_alimento')
        cantidad = data.get('cantidad')
        fecha = data.get('fecha')

        if not id_dieta or not codigo_tabla_tipo_alimento or not cantidad or not fecha:
            flash('Faltan datos obligatorios', 'error')
            return redirect(url_for('alimentacion_blueprint.new_alimentacion_form'))

        id_alimentacion = AlimentacionService.create_alimentacion(
            id_dieta=id_dieta,
            codigo_tabla_tipo_alimento=codigo_tabla_tipo_alimento,
            cantidad=cantidad,
            fecha=fecha,
            tipo_tabla_tipo_alimento=tipo_tabla_tipo_alimento
        )

        if id_alimentacion:
            flash('Alimentación creada exitosamente', 'success')
            return redirect(url_for('alimentacion_blueprint.view_alimentacion', id_alimentacion=id_alimentacion, tipos_alimento=tipos_alimento))
        else:
            flash('Error al crear la alimentación', 'error')
            return render_template('alimentacion/new.html', tipos_alimento=tipos_alimento)

    return render_template('alimentacion/new.html', alimentacion=None, tipos_alimento=tipos_alimento)


@alimentacion_blueprint.route('/edit', methods=['GET', 'POST'])
@AuthService.login_required
def edit_alimentacion_form():
    tipos_alimento = TablaService.get_ftabla_by_id(9)
    if request.method == 'POST':
        id_alimentacion = request.form.get('id_alimentacion')
        alimentacion = AlimentacionService.get_alimentacion_by_id(id_alimentacion)

        if isinstance(alimentacion, list) and len(alimentacion) > 0:
            alimentacion = alimentacion[0]

        if not alimentacion:
            flash('Alimentación no encontrada', 'error')
            return redirect(url_for('alimentacion_blueprint.edit_alimentacion_form'))

        return render_template('alimentacion/edit.html', alimentacion=alimentacion, tipos_alimento=tipos_alimento)

    return render_template('alimentacion/edit.html', alimentacion=None, tipos_alimento=tipos_alimento)


@alimentacion_blueprint.route('/update/<int:id_alimentacion>', methods=['POST'])
@AuthService.login_required
def update_alimentacion(id_alimentacion):
    data = request.form
    tipos_alimento = TablaService.get_ftabla_by_id(9)
    id_dieta = data.get('id_dieta')
    tipo_tabla_tipo_alimento = 9
    codigo_tabla_tipo_alimento = data.get('codigo_tabla_tipo_alimento')
    cantidad = data.get('cantidad')
    fecha = data.get('fecha')

    success = AlimentacionService.update_alimentacion(
        id_alimentacion=id_alimentacion,
        id_dieta=id_dieta,
        codigo_tabla_tipo_alimento=codigo_tabla_tipo_alimento,
        cantidad=cantidad,
        fecha=fecha,
        tipo_tabla_tipo_alimento=tipo_tabla_tipo_alimento
    )

    if success:
        flash('Alimentación actualizada exitosamente', 'success')
        return redirect(url_for('alimentacion_blueprint.view_alimentacion', id_alimentacion=id_alimentacion, tipos_alimento=tipos_alimento))
    else:
        flash('Error al actualizar la alimentación', 'error')
        return redirect(url_for('alimentacion_blueprint.edit_alimentacion_form', alimentacion=None, id_alimentacion=id_alimentacion, tipos_alimento=tipos_alimento))


@alimentacion_blueprint.route('/delete/<int:id_alimentacion>', methods=['POST'])
@AuthService.login_required
def delete_alimentacion(id_alimentacion):
    success = AlimentacionService.delete_alimentacion(id_alimentacion)
    if success:
        flash('Alimentación eliminada exitosamente', 'success')
    else:
        flash('Error al eliminar la alimentación', 'error')
    return redirect(url_for('alimentacion_blueprint.list_alimentaciones'))


@alimentacion_blueprint.route('/get_dieta_info/<int:dieta_id>', methods=['GET'])
@AuthService.login_required
def get_dieta_info(dieta_id):
    try:
        dieta = DietaService.get_dieta_by_id(dieta_id)
        if dieta and len(dieta) > 0:
            dieta_data = dieta[0]
            return jsonify({
                'success': True,
                'id_dieta': dieta_data['id_dieta'],
                'id_animal': dieta_data['id_animal'],
                'tipo_tabla_tipo_dieta': dieta_data['tipo_tabla_tipo_dieta'],
                'codigo_tabla_tipo_dieta': dieta_data['codigo_tabla_tipo_dieta'],
                'descripcion': dieta_data['descripcion'],
                'fecha_inicio': dieta_data['fecha_inicio'],
                'fecha_fin': dieta_data['fecha_fin'],
                'tipo_dieta': dieta_data['tipo_dieta'],
            })
        else:
            return jsonify({'success': False, 'message': 'Animal no encontrado'}), 404
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        return jsonify({'success': False, 'message': 'Error al obtener información del animal'}), 500
