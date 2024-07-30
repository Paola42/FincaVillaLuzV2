from app import db


class Tratamientos(db.Model):
    __tablename__ = 'tratamiento'
    idTratamiento = db.Column(db.Integer, primary_key=True)
    fechaInicioTratamiento     = db.Column(db.Date,nullable=True)
    descripcionTratamiento = db.Column(db.String(255), nullable=False)
    medicamento = db.Column(db.Integer, db.ForeignKey('medicamento.idMedicamento'))
    vacuna = db.Column(db.Integer, db.ForeignKey('vacuna.idVacuna'))
    evento = db.Column(db.Integer, db.ForeignKey('Evento.idEvento'))
    fechaFinTratamiento     = db.Column(db.Date,nullable=True)
    dosis      = db.Column(db.String(255), nullable=False)
    viaAdministracion        = db.Columna(db.String(255), nullable=False)
    observaciones     = db.Column(db.String(255), nullable=False)
    frecuencia      = db.Column(db.String(255), nullable=False)