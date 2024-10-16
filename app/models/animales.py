from app import db


class Animales(db.Model):
    __tablename__ = 'animal'
    idAnimal = db.Column(db.Integer, primary_key=True)
    especieAnimal = db.Column(db.String(255), nullable=False)
    razaAnimal = db.Column(db.String(255), nullable=False)
    sexoAnimal = db.Column(db.String(255), nullable=False)
    fechaNacimiento = db.Column(db.Date, nullable=False)
    pesoAnimal = db.Column(db.String(255), nullable=True)
    padres = db.Column(db.String(255), nullable=True)
    idAnimalPadre = db.Column(db.Integer, nullable=False)
    idAnimalMadre = db.Column(db.Integer, nullable=False)