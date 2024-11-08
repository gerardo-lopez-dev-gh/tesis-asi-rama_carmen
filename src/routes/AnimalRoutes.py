from flask import Blueprint, request, redirect, url_for, render_template, flash
from src.services.AnimalService import AnimalService
from src.services.EmpresaService import EmpresaService
from src.services.TablaService import TablaService
from src.services.AuthService import AuthService

animal_blueprint = Blueprint('animal_blueprint', __name__)


@animal_blueprint.route('/list', methods=['GET'])
@AuthService.login_required
def list_animals():
    animals = AnimalService.get_all_animals()
    return render_template('animal/list.html', animals=animals)


@animal_blueprint.route('/view', methods=['GET', 'POST'])
@AuthService.login_required
def view_animal():
    filter_value = request.args.get('filter_value', '')
    filter_type = request.args.get('filter_type', 'id')

    if filter_value.strip() == "":
        if 'filter_value' in request.args:
            flash('Debes ingresar un valor de búsqueda', 'error')
        return render_template('animal/view.html')

    if filter_type == 'id':
        animales = AnimalService.get_animal_by_id(filter_value)
    else:
        flash('Tipo de filtro no válido', 'error')
        return redirect(url_for('animal_blueprint.list_animals'))

    if not animales:
        flash('Animal no encontrado', 'error')
        return render_template('animal/view.html')

    if isinstance(animales, dict):
        animales = [animales]

    return render_template('animal/view.html', animales=animales)


@animal_blueprint.route('/new', methods=['GET', 'POST'])
@AuthService.login_required
def new_animal_form():
    tipo_animal = TablaService.get_ftabla_by_id(12)
    estado_salud = TablaService.get_ftabla_by_id(5)
    if request.method == 'POST':
        data = request.form
        id_empresa = EmpresaService.get_id()
        tipo_tabla_tipo_animal = 12
        codigo_tabla_tipo_animal = data.get('codigo_tabla_tipo_animal')
        fecha_nacimiento = data.get('fecha_nacimiento')
        peso = data.get('peso')
        tipo_tabla_estado_salud = 5
        codigo_tabla_estado_salud = data.get('codigo_tabla_estado_salud')
        tipo_tabla_estado_registro = 13
        codigo_tabla_estado_registro = 1

        if not id_empresa or not codigo_tabla_tipo_animal or not fecha_nacimiento or not peso or not codigo_tabla_estado_salud:
            flash('Faltan datos obligatorios', 'error')
            return redirect(url_for('animal_blueprint.new_animal_form'))

        id_animal = AnimalService.create_animal(
            id_empresa=id_empresa,
            codigo_tabla_tipo_animal=codigo_tabla_tipo_animal,
            fecha_nacimiento=fecha_nacimiento,
            peso=peso,
            codigo_tabla_estado_salud=codigo_tabla_estado_salud,
            codigo_tabla_estado_registro=codigo_tabla_estado_registro,
            tipo_tabla_tipo_animal=tipo_tabla_tipo_animal,
            tipo_tabla_estado_salud=tipo_tabla_estado_salud,
            tipo_tabla_estado_registro=tipo_tabla_estado_registro
        )

        if id_animal:
            flash('Animal creado exitosamente', 'success')
            return redirect(url_for('animal_blueprint.view_animal', id_animal=id_animal))
        else:
            flash('Error al crear el animal', 'error')
            return render_template('animal/new.html', animal=None, tipo_animal=tipo_animal, estado_salud=estado_salud)

    return render_template('animal/new.html', animal=None, tipo_animal=tipo_animal, estado_salud=estado_salud)


@animal_blueprint.route('/edit', methods=['GET', 'POST'])
@AuthService.login_required
def edit_animal_form():
    tipo_animal = TablaService.get_ftabla_by_id(12)
    estado_salud = TablaService.get_ftabla_by_id(5)
    if request.method == 'POST':
        id_animal = request.form.get('id_animal')

        if not id_animal:
            flash('Debe proporcionar un ID de animal', 'error')
            return redirect(url_for('animal_blueprint.edit_animal_form'))

        animal = AnimalService.get_animal_by_id(id_animal)

        if isinstance(animal, list):
            animal = animal[0] if animal else None

        if not animal:
            flash('Animal no encontrado', 'error')
            return redirect(url_for('animal_blueprint.edit_animal_form'))

        return render_template('animal/edit.html', animal=animal, tipo_animal=tipo_animal, estado_salud=estado_salud)

    return render_template('animal/edit.html', animal=None, tipo_animal=tipo_animal, estado_salud=estado_salud)


@animal_blueprint.route('/update/<int:id_animal>', methods=['POST'])
@AuthService.login_required
def update_animal(id_animal):
    data = request.form
    id_empresa = EmpresaService.get_id()
    tipo_tabla_tipo_animal = 12
    codigo_tabla_tipo_animal = data.get('codigo_tabla_tipo_animal')
    fecha_nacimiento = data.get('fecha_nacimiento')
    peso = data.get('peso')
    tipo_tabla_estado_salud = 5
    codigo_tabla_estado_salud = data.get('codigo_tabla_estado_salud')

    if not id_empresa or not codigo_tabla_tipo_animal or not fecha_nacimiento or not peso or not codigo_tabla_estado_salud:
        flash('Faltan datos obligatorios', 'error')
        return redirect(url_for('animal_blueprint.edit_animal_form', animal=None, id_animal=id_animal))

    success = AnimalService.update_animal(
        id_animal=id_animal,
        id_empresa=id_empresa,
        codigo_tabla_tipo_animal=codigo_tabla_tipo_animal,
        fecha_nacimiento=fecha_nacimiento,
        peso=peso,
        codigo_tabla_estado_salud=codigo_tabla_estado_salud,
        tipo_tabla_tipo_animal=tipo_tabla_tipo_animal,
        tipo_tabla_estado_salud=tipo_tabla_estado_salud
    )

    if success:
        flash('Animal actualizado exitosamente', 'success')
        return redirect(url_for('animal_blueprint.view_animal', id_animal=id_animal))
    else:
        flash('Error al actualizar el animal', 'error')
        return redirect(url_for('animal_blueprint.edit_animal_form', animal=None, id_animal=id_animal))


@animal_blueprint.route('/delete/<int:id_animal>', methods=['POST'])
def delete_animal(id_animal):
    success = AnimalService.delete_animal(id_animal)

    if success:
        flash('Animal eliminado exitosamente', 'success')
    else:
        flash('Error al eliminar el animal', 'error')

    return redirect(url_for('animal_blueprint.list_animals'))
