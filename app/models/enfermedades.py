from app import db


class Enfermedades(db.Model):
    __tablename__ = 'enfermedad'
    idEnfermedad = db.Column(db.Integer, primary_key=True)
    nombreEnfermedad = db.Column(db.String(255), nullable=False)
    sintomasEnfermedad= db.Column(db.String(255), nullable=False)
    detallesAdicionalesEnfermedad = db.Column(db.String(255), nullable=False)
    