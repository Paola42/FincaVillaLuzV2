from app import db

class Praderas(db.Model):
    __tablename__ = 'pradera'
    
    idPradera = db.Column(db.Integer, primary_key=True)
    nombrePradera = db.Column(db.String(255), nullable=False)
    ubicacion = db.Column(db.String(255), nullable=False)
    capacidadCarga = db.Column(db.String(255), nullable=False)
    estadoDePastoreo = db.Column(db.String(255), nullable=False)
    manejos = db.Column(db.String(255), nullable=False)
    aforos = db.Column(db.String(255), nullable=False)
    area = db.Column(db.String(255), nullable=False)

    # Asegúrate de que el nombre de la clave foránea sea correcto
    forraje_id = db.Column(db.Integer, db.ForeignKey('forraje.idForraje'))  
