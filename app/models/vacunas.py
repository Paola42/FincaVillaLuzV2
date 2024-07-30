from app import db


class Vacunas(db.Model):
    __tablename__ = 'vacuna'
    idVacuna = db.Column(db.Integer, primary_key=True)
    nombreVacuna = db.Column(db.String(255), nullable=False)
    dosis = db.Column(db.String(255), nullable=False)
    viaAdministracion = db.Column(db.String(255), nullable=False)
    intervaloReVacunacion = db.Column(db.String(255), nullable=False)
    enfermedadOdjectivo = db.Column(db.String(255), nullable=False)
    tipoVacuna = db.Column(db.String(255), nullable=False)
    planNacional= db.Column(db.String(255), nullable=False)
