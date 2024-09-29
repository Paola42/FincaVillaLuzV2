from flask import Flask
from flask_mail import Mail
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
import os
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config.from_object('config.Config')
    csrf.init_app(app)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    

    @login_manager.user_loader
    def load_user(user_id):
        from .models.administradores import Administrador
        return Administrador.query.get(int(user_id))

    from app.routes import (auth,administrador_routes,operario_routes,aprendiz_routes, instructor_routes, animal_routes, mejoramientogenetico_routes, control_routes, vacuna_routes, aplicacionVacuna_routes,animalmejorado_routes)
    
    app.register_blueprint(administrador_routes.bp)
    app.register_blueprint(operario_routes.bp)
    app.register_blueprint(aprendiz_routes.bp)
    app.register_blueprint(instructor_routes.bp)
    app.register_blueprint(animal_routes.bp)
    app.register_blueprint(mejoramientogenetico_routes.bp)
    app.register_blueprint(control_routes.bp)
    app.register_blueprint(vacuna_routes.bp)
    app.register_blueprint(aplicacionVacuna_routes.bp)
    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(animalmejorado_routes.bp)
#-------------------------------------------------------emails-----------------------
    mail.init_app(app)
    
    return app 


