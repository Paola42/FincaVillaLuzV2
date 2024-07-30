from flask_login import UserMixin
from app import db


class Administrador(db.Model,UserMixin):
    __tablename__ = 'administrador'
    idAdministrador = db.Column(db.Integer, primary_key=True)
    nombreAdministrador = db.Column(db.String(255), nullable=False)
    documentoAdministrador= db.Column(db.String(255), nullable=False)
    direccionAdministrador = db.Column(db.String(255), nullable=False)
    telefonoAdministrador = db.Column(db.String(255), nullable=False)
    correoAdministrador = db.Column(db.String(255), nullable=False)
    passwordAdministrador= db.Column(db.String(255), nullable=False)

    def get_id(self):
        return str(self.idAdministrador)