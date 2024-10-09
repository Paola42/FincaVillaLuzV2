from app import db

class PraderaAnimal(db.Model):
    __tablename__ = 'praderaAnimal'
    idPraderaAnimal = db.Column(db.Integer, primary_key=True)
    idAnimal = db.Column(db.Integer, db.ForeignKey('animal.idAnimal'))
    idPradera = db.Column(db.Integer, db.ForeignKey('pradera.idPradera'))
    cantidad = db.Column(db.Integer, nullable=False)
