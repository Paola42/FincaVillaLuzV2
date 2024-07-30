from app import db


class Eventos(db.Model):
    __tablename__ = 'evento'
    idEvento = db.Column(db.Integer, primary_key=True)
    animal= db.Column(db.Integer, db.ForeignKey('animal.idAnimal'))
    enfermedad= db.Column(db.Integer, db.ForeignKey('enfermedad.idEnfermedad'))
    instructor= db.Column(db.Integer, db.ForeignKey('instructor.idInstructor'))