from flask import Blueprint

bp = Blueprint('main', __name__)

from app.routes import auth,administrador_routes,aprendiz_routes,instructor_routes,operario_routes