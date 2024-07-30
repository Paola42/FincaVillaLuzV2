from app import db


class MejoramientosGeneticos(db.Model):
    __tablename__ = 'mejoramientoGenetico'
    idMejoramientoGenetico = db.Column(db.Integer, primary_key=True)
    tecnicaEventoGenetico = db.Column(db.String(255), nullable=False)
    fechaEvento     = db.Column(db.Date,nullable=True)
    resultados      = db.Column(db.String(255), nullable=False)
    detalles        = db.Columna(db.String(255), nullable=False)
    animalMejorado  = db.Column(db.Integer, db.ForeignKey('animalMejorado.idAnimalMejorado'))