from flask import Blueprint

bp = Blueprint('main', __name__)


from app.routes import auth,administrador_routes,aprendiz_routes,instructor_routes,operario_routes,animal_routes, animalmejorado_routes, mejoramientogenetico_routes, control_routes



