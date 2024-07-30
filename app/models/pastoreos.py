from app import db


class Pastoreos(db.Model):
    __tablename__ = 'pastoreo'
    idPastoreo = db.Column(db.Integer, primary_key=True)
    fechaInicioPastoreo =db.Column(db.db.Date,nullable=True)
    fechaFinPastoreo =db.Column(db.db.Date,nullable=True)
    duracionPastoreo = db.Column(db.String(255), nullable=False)
    CargaAnimal  = db.Column(db.String(255), nullable=False)
    horasDePastoreo  =db.column(db.String(255),nullable=True)
    