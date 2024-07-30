from app import db


class Forrajes(db.Model):
    __tablename__ = 'forraje'
    idForraje = db.Column(db.Integer, primary_key=True)
    especie= db.Column(db.String(255), nullable=False)
    fechaDeSiembra =db.Column(db.db.Date,nullable=True)
    fechaDeCosecha =db.Column(db.db.Date,nullable=True)
    area = db.Column(db.String(255), nullable=False)
    manejos  = db.Column(db.String(255), nullable=False)
    aforo  =db.column(db.String(255),nullable=True)
    forraje  = db.Column(db.Integer, db.ForeignKey('forraje.idForraje'))