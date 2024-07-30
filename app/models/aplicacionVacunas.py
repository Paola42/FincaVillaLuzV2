from app import db


class AplicacionVacunas(db.Model):
    __tablename__ = 'aplicacionVacuna'
    idAplicacionVacuna= db.Column(db.Integer, primary_key=True)
    fechaAplicacion=db.Column(db.Date,nullable=True)
    animal= db.Column(db.Integer, db.ForeignKey('animal.idAnimal'))
    vacuna = db.Column(db.Integer, db.ForeignKey('vacuna.idVacuna'))