from app import db


class Enfermedades(db.Model):
    __tablename__ = 'enfermedad'
    idEnfermedad = db.Column(db.Integer, primary_key=True)
    nombreEnfermedad = db.Column(db.String(255), nullable=False)
    sintomas= db.Column(db.String(255), nullable=False)
    detallesAdicionales = db.Column(db.String(255), nullable=False)
    