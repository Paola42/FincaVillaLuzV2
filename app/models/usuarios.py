from flask_login import UserMixin
from app import db

class Usuarios(db.Model, UserMixin):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre    = db.Column(db.String(80), unique=True, nullable=False)
    documento =db.Column(db.String(80),nullable=False)
    direccion =db.Column(db.String(80),nullable=False)
    telefono  =db.Column(db.String(80),nullable=False)
    correo    =db.Column(db.String(80),nullable=False)
    password  = db.Column(db.String(120), nullable=False)
    tipo      =db.Column(db.String(80),nullable=False)  