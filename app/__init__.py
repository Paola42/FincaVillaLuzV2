from flask import Flask, redirect, url_for, render_template, request, make_response
from flask_mail import Mail
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
import os

# Instanciación de extensiones
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()




def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Importa tu configuración desde config.py
    mail = Mail(app)

    # Configuración de la aplicación
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config.from_object('config.Config')

    # Inicialización de extensiones
    csrf.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # Configuración de Flask-Login
    login_manager.login_view = 'auth.login'

    # Manejador personalizado para usuarios no autorizados
    @login_manager.unauthorized_handler
    def unauthorized_callback():
        return redirect(url_for('auth.principal'))

    @login_manager.user_loader
    def load_user(user_id):
        from .models.administradores import Administrador
        return Administrador.query.get(int(user_id))

    # Rutas para manejar cookies
    @app.route('/set_cookie')
    def set_cookie():
        # Crear una respuesta
        resp = make_response("Cookie configurada con éxito")
        # Establecer una cookie llamada 'mi_cookie' con el valor 'valor_cookie'
        resp.set_cookie('mi_cookie', 'valor_cookie', max_age=60*60*24)  # 1 día
        return resp

    @app.route('/get_cookie')
    def get_cookie():
        # Obtener el valor de la cookie
        valor_cookie = request.cookies.get('mi_cookie')
        return f"El valor de la cookie es: {valor_cookie}"

    @app.route('/delete_cookie')
    def delete_cookie():
        # Crear una respuesta y eliminar la cookie
        resp = make_response("Cookie eliminada")
        resp.set_cookie('mi_cookie', '', max_age=0)  # max_age=0 para eliminar la cookie
        return resp

    # Registro de blueprints
    from app.routes import (
        auth,
        administrador_routes,
        operario_routes,
        aprendiz_routes,
        instructor_routes,
        animal_routes,
        mejoramientogenetico_routes,
        control_routes,
        vacuna_routes,
        aplicacionvacuna_routes,
        animalmejorado_routes,
        pastoreo_routes,
        forraje_routes,
        pradera_routes,
        medicamento_routes,
        evento_routes,
        enfermedad_routes,
        tratamiento_routes,
        praderaAnimal_routes
    )

    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(administrador_routes.bp)
    app.register_blueprint(operario_routes.bp)
    app.register_blueprint(aprendiz_routes.bp)
    app.register_blueprint(instructor_routes.bp)
    app.register_blueprint(animal_routes.bp)
    app.register_blueprint(mejoramientogenetico_routes.bp)
    app.register_blueprint(control_routes.bp)
    app.register_blueprint(vacuna_routes.bp)
    app.register_blueprint(aplicacionvacuna_routes.bp)
    app.register_blueprint(animalmejorado_routes.bp)
    app.register_blueprint(pastoreo_routes.bp)
    app.register_blueprint(forraje_routes.bp)
    app.register_blueprint(pradera_routes.bp)
    app.register_blueprint(medicamento_routes.bp)
    app.register_blueprint(evento_routes.bp)
    app.register_blueprint(enfermedad_routes.bp)
    app.register_blueprint(tratamiento_routes.bp)
    app.register_blueprint(praderaAnimal_routes.bp)

    return app
