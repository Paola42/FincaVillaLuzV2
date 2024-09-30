from app import db

class Forrajes(db.Model):
    __tablename__ = 'forraje'
    idForraje = db.Column(db.Integer, primary_key=True)
    especieForraje = db.Column(db.String(255), nullable=False)
    fechaDeSiembraForraje = db.Column(db.Date, nullable=True)
    fechaDeCosechaForraje = db.Column(db.Date, nullable=True)
    areaForraje = db.Column(db.String(255), nullable=False)
    manejosForraje = db.Column(db.String(255), nullable=False)
    aforoForraje = db.Column(db.String(255), nullable=True)

