from app import db


class Animales(db.Model):
    __tablename__ = 'animal'
    idAnimal = db.Column(db.Integer, primary_key=True)
    especieAnimal= db.Column(db.String(255), nullable=False)
    razaAnimal = db.Column(db.String(255), nullable=False)
    sexoAnimal  = db.Column(db.String(255), nullable=False)
    fechaNacimiento =db.Column(db.db.Date,nullable=True)
    pesoAnimal         =db.column(db.String(255),nullable=True)
    padres =db.column(db.String(255),nullable=True)
    idAnimalPadre = db.column(db.Integer,nullable=False)
    idAnimalMadre = db.column(db.Integer,nullable=False)