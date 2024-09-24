from flask import Blueprint

bp = Blueprint('main', __name__)


from app.routes import auth,administrador_routes,aprendiz_routes,instructor_routes,operario_routes,animal_routes, animalmejorado_routes, aplicacionvacuna_routes, control_routes,enfermedad_routes, evento_routes, forraje_routes,medicamento_routes, mejoramientogenetico_routes, pastoreo_routes,pradera_routes,tratamiento_routes, vacuna_routes



