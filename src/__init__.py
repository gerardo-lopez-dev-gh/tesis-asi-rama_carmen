from flask import Flask
from .routes import AuthRoutes, IndexRoutes, AnimalRoutes, ConfigRoutes, UserRoutes, GeneralRoutes, DietaRoutes, AlimentacionRoutes, HistorialMedicoRoutes, TratamientosRoutes, TratamientosAplicadosRoutes, MedidasPreventivasRoutes, UsuariosRolesRoutes, RolPermisoRoutes, MateriaPrimaRoutes, RolesRoutes, AuditoriaRoutes, MonedaRoutes, VentasRoutes

# Inicializa la aplicación Flask
app = Flask(__name__)


def init_app(config):
    """
    Inicializa la aplicación Flask con la configuración proporcionada y registra los blueprints.

    :param config: Objeto de configuración que contiene las variables de configuración de la aplicación.
    :return: La instancia de la aplicación Flask.
    """
    # Aplicar la configuración desde el objeto config
    app.config.from_object(config)

    # Registro de los Blueprints con sus respectivos prefijos de URL
    app.register_blueprint(IndexRoutes.index_blueprint, url_prefix='/')
    app.register_blueprint(AuthRoutes.auth_blueprint, url_prefix='/auth')
    app.register_blueprint(AnimalRoutes.animal_blueprint, url_prefix='/animal')
    #app.register_blueprint(ConfigRoutes.config_blueprint, url_prefix='/config')
    app.register_blueprint(UserRoutes.user_blueprint, url_prefix='/user')
    app.register_blueprint(GeneralRoutes.general_blueprint, url_prefix='/general')
    app.register_blueprint(DietaRoutes.dieta_blueprint, url_prefix='/dietas')
    app.register_blueprint(AlimentacionRoutes.alimentacion_blueprint, url_prefix='/alimentacion')
    app.register_blueprint(HistorialMedicoRoutes.historialmed_blueprint, url_prefix='/historialmedico')
    app.register_blueprint(TratamientosRoutes.tratamiento_blueprint, url_prefix='/tratamientos')
    app.register_blueprint(TratamientosAplicadosRoutes.tratamiento_aplicado_blueprint, url_prefix='/tratamientosaplicados')
    app.register_blueprint(MedidasPreventivasRoutes.medidasprev_blueprint, url_prefix='/medidaspreventivas')
    app.register_blueprint(MateriaPrimaRoutes.materiaprima_blueprint, url_prefix='/materiasprimas')
    app.register_blueprint(RolesRoutes.roles_blueprint, url_prefix='/roles')
    app.register_blueprint(MonedaRoutes.monedas_blueprint, url_prefix='/monedas')
    app.register_blueprint(VentasRoutes.ventas_blueprint, url_prefix='/ventas')

    #app.register_blueprint(RolesRoutes.roles_blueprint, url_prefix='/permisos')
    app.register_blueprint(UsuariosRolesRoutes.usuariosrol_blueprint, url_prefix='/usuariosrol')
    app.register_blueprint(RolPermisoRoutes.rolpermiso_blueprint, url_prefix='/permisosroles')
    app.register_blueprint(AuditoriaRoutes.auditoria_blueprint, url_prefix='/auditoria')
    return app
