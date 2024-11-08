from flask import Blueprint, render_template, jsonify, request
import traceback
from src.utils.Logger import Logger
from src.services.AuthService import AuthService

index_blueprint = Blueprint('index_blueprint', __name__)


@index_blueprint.route('/home')
def index():
    try:
        Logger.add_to_log("info", "{} {}".format(request.method, request.path))
        return render_template('home/home.html')
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

        response = jsonify({'message': "Internal Server Error Menu", 'success': False})
        return response, 500


@index_blueprint.route('/about')
def about():
    try:
        Logger.add_to_log("info", "{} {}".format(request.method, request.path))
        return render_template('home/about.html')
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

        response = jsonify({'message': "Internal Server Error", 'success': False})
        return response, 500


@index_blueprint.route('/contact')
def contact():
    try:
        Logger.add_to_log("info", "{} {}".format(request.method, request.path))
        return render_template('home/contact.html')
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

        response = jsonify({'message': "Internal Server Error", 'success': False})
        return response, 500


@index_blueprint.route('/menu')
@AuthService.login_required
def menu():
    try:
        Logger.add_to_log("info", "{} {}".format(request.method, request.path))
        return render_template('home/menu.html')
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

        response = jsonify({'message': "Internal Server Error", 'success': False})
        return response, 500
