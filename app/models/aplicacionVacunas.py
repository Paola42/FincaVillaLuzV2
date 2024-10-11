from app import db

class AplicacionVacunas(db.Model):
    __tablename__ = 'aplicacionVacuna'
    idAplicacionVacuna = db.Column(db.Integer, primary_key=True)
    fechaAplicacion = db.Column(db.Date, nullable=True)
    idAnimal = db.Column(db.Integer, db.ForeignKey('animal.idAnimal'))  
    idVacuna = db.Column(db.Integer, db.ForeignKey('vacunas.idVacuna'))
    idInstructor = db.Column(db.Integer, db.ForeignKey('instructor.idInstructor'))  
    
