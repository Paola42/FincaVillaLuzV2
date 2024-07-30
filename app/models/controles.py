from app import db


class Controles(db.Model):
    __tablename__ = 'control'
    idControl = db.Column(db.Integer, primary_key=True)
    descripcion= db.Column(db.String(255), nullable=False)
    fecha=db.Column(db.Date,nullable=True)
    estado= db.Column(db.String(255), nullable=False)
    animalMejorado= db.Column(db.Integer, db.ForeignKey('animalMejorado.idAnimalMejorado'))