from flask import Flask
from flask_mail import Mail
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os
db = SQLAlchemy()
login_manager = LoginManager()

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    

    @login_manager.user_loader
    def load_user(user_id):
        from .models.administradores import Administrador
        return Administrador.query.get(int(user_id))

    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    from app.routes import (auth,administrador_routes,operario_routes,aprendiz_routes, instructor_routes, animal_routes, animalmejorado_routes, aplicacionvacuna_routes)
    
    app.register_blueprint(administrador_routes.bp)
    app.register_blueprint(operario_routes.bp)
    app.register_blueprint(aprendiz_routes.bp)
    app.register_blueprint(instructor_routes.bp)
    app.register_blueprint(animal_routes.bp)
    app.register_blueprint(animalmejorado_routes.bp)
    app.register_blueprint(aplicacionvacuna_routes.bp)
    
#-------------------------------------------------------emails-----------------------
   
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'juanespitia538@gmail.com'
    app.config['MAIL_PASSWORD'] = '1101752867'
    app.config['MAIL_DEFAULT_SENDER'] = 'juanespitia538@gmail.com'
    
    mail.init_app(app)
    
    return app 


