from flask_login import UserMixin
from app import db


class Operarios(db.Model,UserMixin):
    __tablename__ = 'operarios'
    idOperario        = db.Column(db.Integer, primary_key=True)
    nombreOperario     = db.Column(db.String(255), nullable=False)
    documentoOperario  = db.Column(db.String(255), nullable=False)
    direccionOperario  = db.Column(db.String(255), nullable=False)
    telefonoOperario   = db.Column(db.String(255), nullable=False)
    corre      = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def get_id(self):
        return str(self.idOperario)