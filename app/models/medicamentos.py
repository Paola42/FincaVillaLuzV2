from app import db


class Medicamentos(db.Model):
    __tablename__ = 'medicamento'
    idMedicamento = db.Column(db.Integer, primary_key=True)
    nombreMedicamento = db.Column(db.String(255), nullable=False)
    dosis= db.Column(db.String(255), nullable=False)
    viaAdministracion = db.Column(db.String(255), nullable=False)
    indicaciones  = db.Columnn(db.String(255),nullable=False)
    contraindicaciones  = db.Columnn(db.String(255),nullable=False)