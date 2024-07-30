from flask_login import UserMixin
from app import db


class Instructores(db.Model,UserMixin):
    __tablename__ = 'instructor'
    idInstructor = db.Column(db.Integer, primary_key=True)
    nombreInstructor = db.Column(db.String(255), nullable=False)
    documentoInstructor= db.Column(db.String(255), nullable=False)
    direccionInstructor = db.Column(db.String(255), nullable=False)
    telefonoInstructor = db.Column(db.String(255), nullable=False)
    correo = db.Column(db.String(255), nullable=False)
    Password= db.Column(db.String(255), nullable=False)

    def get_id(self):
        return str(self.idInstructor)