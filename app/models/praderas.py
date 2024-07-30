from app import db


class Praderas(db.Model):
    __tablename__ = 'pradera'
    idPradera = db.Column(db.Integer, primary_key=True)
    nombrePradera = db.Column(db.String(255), nullable=False)
    ubicacion= db.Column(db.String(255), nullable=False)
    capacidadCarga = db.Column(db.String(255), nullable=False)
    estadoDePastoreo  = db.Columnn(db.String(255),nullable=False)
    manejos  = db.Columnn(db.String(255),nullable=False)
    aforos = db.Columnn(db.String(255),nullable=False)
    area  = db.Columnn(db.String(255),nullable=False)
    forraje  = db.Column(db.Integer, db.ForeignKey('forraje.idforraje')) 
    pastoreo  = db.Column(db.Integer, db.ForeignKey('pastoreo.idPastoreo'))