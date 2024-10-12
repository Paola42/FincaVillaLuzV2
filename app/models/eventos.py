from app import db


class Eventos(db.Model):
    __tablename__ = 'evento'
    idEvento = db.Column(db.Integer, primary_key=True)
    idAnimal= db.Column(db.Integer, db.ForeignKey('animal.idAnimal'))
    idEnfermedad= db.Column(db.Integer, db.ForeignKey('enfermedad.idEnfermedad'))
    idInstructor= db.Column(db.Integer, db.ForeignKey('instructor.idInstructor'))   