from flask_login import UserMixin
from app import db


class Aprendices(db.Model,UserMixin):
    __tablename__ = 'aprendiz'
    idAprendiz        = db.Column(db.Integer, primary_key=True)
    nombreAprendiz    = db.Column(db.String(255), nullable=False)
    documentoAprendiz = db.Column(db.String(255), nullable=False)
    direccionAprendiz = db.Column(db.String(255), nullable=False)
    direccionAprendiz  = db.Column(db.String(255), nullable=False)
    correoAprendiz    = db.Column(db.String(255), nullable=False)
    passwordAprendiz= db.Column(db.String(255), nullable=False)

    def get_id(self):
        return str(self.idAprendiz)