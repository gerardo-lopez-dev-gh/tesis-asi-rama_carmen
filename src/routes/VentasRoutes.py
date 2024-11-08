from flask import Blueprint, request, redirect, url_for, render_template, flash
from src.services.VentasService import VentasService
from src.services.VentaDetalleService import VentaDetalleService
from src.services.AuthService import AuthService
from src.services.GeneralService import GeneralService
from flask import jsonify
from src.utils.Logger import Logger


ventas_blueprint = Blueprint('ventas_blueprint', __name__)


@ventas_blueprint.route('/list/', methods=['GET'])
@AuthService.login_required
def list_ventas():
    ventas = VentasService.get_all_ventas()
    return render_template('ventas/list.html', ventas=ventas)


@ventas_blueprint.route('/view', methods=['GET'])
@AuthService.login_required
def view_venta():
    filter_value = request.args.get('filter_value', '')
    filter_type = request.args.get('filter_type', 'id')

    if filter_value.strip() == "":
        if 'filter_value' in request.args:
            flash('Debes ingresar un valor de búsqueda', 'error')
        return render_template('ventas/view.html')

    if filter_type == 'id':
        ventas = VentasService.get_venta_by_id(filter_value)
    else:
        flash('Tipo de filtro no válido', 'error')
        return redirect(url_for('ventas_blueprint.list_ventas'))

    if not ventas:
        flash('Registro de venta no encontrada', 'error')
        return render_template('ventas/view.html')

    if isinstance(ventas, dict):
        ventas = [ventas]

    detalle = VentaDetalleService.get_venta_detalle_by_id(ventas.id_venta)

    if isinstance(detalle, dict):
        detalle = [detalle]

    return render_template('ventas/view.html', ventas=ventas, detalle=detalle)


@ventas_blueprint.route('/new', methods=['GET', 'POST'])
@AuthService.login_required
def new_venta_form():
    if request.method == 'POST':
        data = request.form
        id_cliente = data.get('id_persona')
        fecha_venta = data.get('fecha_venta')
        cantidad_vendida = 0
        precio_total = 0
        moneda = data.get('moneda')

        if not id_cliente or not fecha_venta or not moneda:
            flash('Faltan datos obligatorios ', 'error')
            return redirect(url_for('ventas_blueprint.new_venta_form'))

        id_venta = VentasService.create_venta(
            id_cliente=id_cliente,
            fecha_venta=fecha_venta,
            cantidad_vendida=cantidad_vendida,
            precio_total=precio_total,
            moneda=moneda
        )

        if id_venta:
            flash('Venta registrada exitosamente', 'success')
            return redirect(url_for('ventas_blueprint.view_venta', id_venta=id_venta))
        else:
            flash('Error al registrar la venta', 'error')
            return render_template('ventas/new.html')

    return render_template('ventas/new.html')


@ventas_blueprint.route('/add_detalle/<int:id_venta>', methods=['GET', 'POST'])
@AuthService.login_required
def add_venta_detalle(id_venta):
    if request.method == 'POST':
        data = request.form
        id_producto_final = data.get('id_producto_final')
        cantidad = float(data.get('cantidad'))
        precio_unitario = float(data.get('precio_unitario'))
        total_item = round(cantidad * precio_unitario)

        if not id_producto_final or not cantidad or not precio_unitario:
            flash('Todos los campos de detalle son obligatorios', 'error')
            return redirect(url_for('ventas_blueprint.add_venta_detalle', id_venta=id_venta))

        # Insertar detalle de la venta
        VentaDetalleService.create_venta_detalle(
            id_producto_final=id_producto_final,
            id_venta=id_venta,
            cantidad=cantidad,
            precio_unitario=precio_unitario,
            total_item=total_item
        )

        # Actualizar la cantidad total vendida y el precio total de la venta
        venta = VentasService.get_venta_by_id(id_venta)

        VentasService.update_venta_totals(venta.id_venta, venta.id_cliente, venta.fecha_venta, venta.moneda)

        flash('Detalle agregado exitosamente', 'success')
        return redirect(url_for('ventas_blueprint.add_venta_detalle', id_venta=id_venta))

    return render_template('ventas/add_detalle.html', id_venta=id_venta)


@ventas_blueprint.route('/edit', methods=['GET', 'POST'])
@AuthService.login_required
def edit_venta_form():
    if request.method == 'POST':
        id_venta = request.form.get('id_historial')

        if not id_venta:
            flash('Debe proporcionar un ID del registro de venta', 'error')
            return redirect(url_for('ventas_blueprint.edit_venta_form'))

        ventas = VentasService.get_venta_by_id(id_venta)

        if isinstance(ventas, list):
            ventas = ventas[0] if ventas else None

        if not ventas:
            flash('Venta no encontrada', 'error')
            return redirect(url_for('ventas_blueprint.edit_venta_form'))

        return render_template('ventas/edit.html', ventas=ventas)

    return render_template('ventas/edit.html')


@ventas_blueprint.route('/update/<int:id_venta>', methods=['POST'])
@AuthService.login_required
def update_venta(id_venta):
    data = request.form
    id_cliente = data.get('id_cliente')
    fecha_venta = data.get('fecha_venta')
    cantidad_vendida = data.get('cantidad_vendida')
    precio_total = data.get('precio_total')
    moneda = data.get('moneda')

    if not id_cliente or not fecha_venta or not cantidad_vendida or not precio_total or not moneda:
        flash('Faltan datos obligatorios', 'error')
        return redirect(url_for('ventas_blueprint.edit_venta_form', id_venta=id_venta))

    success = VentasService.update_venta(
        id_venta=id_venta,
        id_cliente=id_cliente,
        fecha_venta=fecha_venta,
        cantidad_vendida=cantidad_vendida,
        precio_total=precio_total,
        moneda=moneda
    )

    if success:
        flash('Registro de venta actualizada exitosamente', 'success')
        return redirect(url_for('ventas_blueprint.edit_venta_form', id_venta=id_venta))
    else:
        flash('Error al actualizar el registro de venta', 'error')
        return redirect(url_for('ventas_blueprint.edit_venta_form', id_venta=id_venta))


@ventas_blueprint.route('/get_cliente_info/<int:cliente_id>', methods=['GET'])
@AuthService.login_required
def get_cliente_info(cliente_id):
    try:
        cliente = GeneralService.get_person_by_id(cliente_id)
        if cliente and len(cliente) > 0:
            cliente_data = cliente[0]
            return jsonify({
                'success': True,
                'id_persona': cliente_data['id_persona'],
                'nombre': cliente_data['nombre'],
                'direccion': cliente_data['direccion'],
                'telefono': cliente_data['telefono'],
                'correo_electronico': cliente_data['correo_electronico'],
                'tipo_tabla_estado_civil': cliente_data['tipo_tabla_estado_civil'],
                'codigo_tabla_estado_civil': cliente_data['codigo_tabla_estado_civil'],
                'documento': cliente_data['documento'],
                'tipo_tabla_tipo_documento': cliente_data['tipo_tabla_tipo_documento'],
                'codigo_tabla_tipo_documento': cliente_data['codigo_tabla_tipo_documento'],
                'tipo_tabla_estado_registro': cliente_data['tipo_tabla_estado_registro'],
                'codigo_tabla_estado_registro': cliente_data['codigo_tabla_estado_registro'],
                'tipo_tabla_tipo_registro': cliente_data['tipo_tabla_tipo_registro'],
                'codigo_tabla_tipo_registro': cliente_data['codigo_tabla_tipo_registro'],
                'estado_civil': cliente_data['estado_civil'],
                'tipo_documento': cliente_data['tipo_documento'],
                'estado_registro': cliente_data['estado_registro'],
                'tipo_registro': cliente_data['tipo_registro'],
            })
        else:
            return jsonify({'success': False, 'message': 'Cliente no encontrado'}), 404
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        return jsonify({'success': False, 'message': 'Error al obtener información del cliente'}), 500
