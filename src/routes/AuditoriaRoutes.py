from flask import Blueprint, request, redirect, url_for, render_template, flash
from src.services.AuditoriaService import AuditoriaService
from src.services.AuthService import AuthService

auditoria_blueprint = Blueprint('auditoria_blueprint', __name__)


@auditoria_blueprint.route('/list', methods=['GET'])
@AuthService.login_required
def list_histo_audi():
    histo_audi = AuditoriaService.get_all_auditoria()
    return render_template('auditoria/list.html', histo_audi=histo_audi)


@auditoria_blueprint.route('/view', methods=['GET'])
@AuthService.login_required
def view_histo_audi():
    filter_value = request.args.get('filter_value', '')
    filter_type = request.args.get('filter_type', 'id')

    if filter_value.strip() == "":
        if 'filter_value' in request.args:
            flash('Debes ingresar un valor de búsqueda', 'error')
        return render_template('auditoria/view.html')

    if filter_type == 'id':
        histo_audi = AuditoriaService.get_auditoria_by_id(filter_value)
    else:
        flash('Tipo de filtro no válido', 'error')
        return redirect(url_for('auditoria_blueprint.list_histo_audi'))

    if not histo_audi:
        flash('Registro de auditoría no encontrado', 'error')
        return render_template('auditoria/view.html')

    if isinstance(histo_audi, dict):
        histo_audi = [histo_audi]

    return render_template('auditoria/view.html', histo_audi=histo_audi)
