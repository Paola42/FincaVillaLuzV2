from app import db

class AnimalesMejorados(db.Model):
    __tablename__ = 'animalMejorado'

    idAnimalMejorado    = db.Column(db.Integer, primary_key=True)
    idPadreAportante    = db.column(db.Integer,nullable=False)
    nombrePadreAportante = db.Column(db.String(255), nullable=False)
    razaPadreAportante       = db.Column(db.String(255), nullable=False)
    idMadreAportante    = db.column(db.Integer,nullable=False)
    nombreMadreAportante        = db.Column(db.String(255), nullable=False)
    razaMadreAportante  = db.Column(db.String(255), nullable=False)
    animal= db.Column(db.Integer, db.ForeignKey('animal.idAnimal'))