from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os
db = SQLAlchemy()
login_manager = LoginManager()

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

    from app.routes import (auth,administrador_routes,operario_routes,aprendiz_routes,instructor_routes, animal_routes)
    
    app.register_blueprint(administrador_routes.bp)
    app.register_blueprint(operario_routes.bp)
    app.register_blueprint(aprendiz_routes.bp)
    app.register_blueprint(instructor_routes.bp)
    app.register_blueprint(animal_routes.bp)

   

    return app 