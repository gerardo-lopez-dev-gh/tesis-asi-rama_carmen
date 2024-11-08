from flask import Blueprint, request, redirect, url_for, render_template, flash
from src.services.MonedaService import MonedaService
from src.services.TablaService import TablaService
from src.services.AuthService import AuthService


monedas_blueprint = Blueprint('monedas_blueprint', __name__)


@monedas_blueprint.route('/list', methods=['GET'])
@AuthService.login_required
def list_monedas():
    monedas = MonedaService.get_all_monedas()
    return render_template('monedas/list.html', monedas=monedas)


@monedas_blueprint.route('/view', methods=['GET'])
@AuthService.login_required
def view_moneda():
    filter_value = request.args.get('filter_value', '')
    filter_type = request.args.get('filter_type', 'id')

    if filter_value.strip() == "":
        if 'filter_value' in request.args:
            flash('Debes ingresar un valor de búsqueda', 'error')
        return render_template('monedas/view.html')

    if filter_type == 'id':
        monedas = MonedaService.get_moneda_by_id(filter_value)
    else:
        flash('Tipo de filtro no válido', 'error')
        return redirect(url_for('monedas_blueprint.list_monedas'))

    if not monedas:
        flash('Moneda no encontrada', 'error')
        return render_template('monedas/view.html')

    if isinstance(monedas, dict):
        monedas = [monedas]

    return render_template('monedas/view.html', monedas=monedas)


@monedas_blueprint.route('/new', methods=['GET', 'POST'])
@AuthService.login_required
def new_moneda_form():
    tipo_moneda = TablaService.get_ftabla_by_id(15)
    if request.method == 'POST':
        data = request.form
        nombre = data.get('nombre').upper()
        tipo_tabla_tipo_moneda = 15
        codigo_tabla_tipo_moneda = data.get('codigo_tabla_tipo_moneda')

        if not nombre or not codigo_tabla_tipo_moneda:
            flash('Faltan datos obligatorios ', 'error')
            return redirect(url_for('monedas_blueprint.new_moneda_form'))

        id_moneda = MonedaService.create_moneda(
            nombre=nombre,
            codigo_tabla_tipo_moneda=codigo_tabla_tipo_moneda,
            tipo_tabla_tipo_moneda=tipo_tabla_tipo_moneda
        )

        if id_moneda:
            flash('Moneda creada exitosamente', 'success')
            return redirect(url_for('monedas_blueprint.view_moneda', id_moneda=id_moneda))
        else:
            flash('Error al crear el moneda', 'error')
            return render_template('monedas/new.html', monedas=None, tipo_moneda=tipo_moneda)

    return render_template('monedas/new.html', monedas=None, tipo_moneda=tipo_moneda)


@monedas_blueprint.route('/edit', methods=['GET', 'POST'])
@AuthService.login_required
def edit_moneda_form():
    tipo_moneda = TablaService.get_ftabla_by_id(15)
    if request.method == 'POST':
        id_moneda = request.form.get('id_moneda')
        nombre = request.form.get('nombre').upper()
        codigo_tabla_tipo_moneda = request.form.get('codigo_tabla_tipo_moneda')

        if not id_moneda or not nombre or not codigo_tabla_tipo_moneda:
            flash('Debe proporcionar un ID de moneda', 'error')
            return redirect(url_for('monedas_blueprint.edit_moneda_form'))

        monedas = MonedaService.get_moneda_by_id(id_moneda)

        if isinstance(monedas, list):
            monedas = monedas[0] if monedas else None

        if not monedas:
            flash('Moneda no encontrada', 'error')
            return redirect(url_for('monedas_blueprint.edit_moneda_form'))

        return render_template('monedas/edit.html', monedas=monedas, tipo_moneda=tipo_moneda)

    return render_template('monedas/edit.html', monedas=None, tipo_moneda=tipo_moneda)


@monedas_blueprint.route('/update/<int:id_moneda>', methods=['POST'])
@AuthService.login_required
def update_moneda(id_moneda):
    data = request.form
    nombre = data.get('nombre').upper()
    tipo_tabla_tipo_moneda = 15
    codigo_tabla_tipo_moneda = data.get('codigo_tabla_tipo_moneda')

    if not nombre or not codigo_tabla_tipo_moneda:
        flash('Faltan datos obligatorios', 'error')
        return redirect(url_for('monedas_blueprint.edit_moneda_form', id_moneda=id_moneda))

    success = MonedaService.update_moneda(
        id_moneda=id_moneda,
        nombre=nombre,
        codigo_tabla_tipo_moneda=codigo_tabla_tipo_moneda,
        tipo_tabla_tipo_moneda=tipo_tabla_tipo_moneda
    )

    if success:
        flash('Moneda actualizada exitosamente', 'success')
        return redirect(url_for('monedas_blueprint.view_moneda', id_moneda=id_moneda))
    else:
        flash('Error al actualizar el moneda', 'error')
        return redirect(url_for('monedas_blueprint.edit_moneda_form', id_moneda=id_moneda))
