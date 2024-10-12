from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.aplicacionVacunas import AplicacionVacunas
from app.models.animales import Animales
from app.models.instructores import Instructores
from app.models.vacunas import Vacunas
from app import db

#   Rutas - Aplicacion Vacunas
bp = Blueprint('aplicacionvacuna', __name__)


#   Index
@bp.route('/AplicacionVacunas')
def index():
    vacuna = AplicacionVacunas.query.all()
    return render_template('aplicacionVacuna/index.html', vacunas = vacuna)


#   Add
@bp.route('/AplicacionVacunas/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        fechaAplicacion = request.form['fechaAplicacion']
        idAnimal = request.form['idAnimal']
        idVacuna = request.form['idVacuna']
        idInstructor = request.form['idInstructor']

        newAplicacionVacuna = AplicacionVacunas(fechaAplicacion=fechaAplicacion, idAnimal=idAnimal, idVacuna=idVacuna, idInstructor=idInstructor)
        db.session.add(newAplicacionVacuna)
        db.session.commit()

        return redirect(url_for('aplicacionvacuna.index'))
    
    animal = Animales.query.all()
    vacuna = Vacunas.query.all()
    instructor = Instructores.query.all()
    
    return render_template('aplicacionVacuna/add.html',animales=animal,vacunas=vacuna,instructores=instructor)


#   Edit
@bp.route('/AplicacionVacunas/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    aplicacionVacuna = AplicacionVacunas.query.get_or_404(id)
    if request.method == 'POST':
        aplicacionVacuna.fechaAplicacion = request.form['fechaAplicacion']
        aplicacionVacuna.idAnimal = request.form['idAnimal']
        aplicacionVacuna.idVacuna = request.form['idVacuna']
        aplicacionVacuna.idInstructor = request.form['idInstructor']

        db.session.commit()
        
        return redirect(url_for('aplicacionvacuna.index'))
    
    dataAnimales = Animales.query.all()
    dataInstructores = Instructores.query.all()
    dataVacunas = Vacunas.query.all()

    return render_template('aplicacionVacuna/edit.html', aplicacionVacuna=aplicacionVacuna, dataAnimales=dataAnimales, dataInstructores=dataInstructores, dataVacunas=dataVacunas)


#   Delete
@bp.route('/AplicacionVacunas/delete/<int:id>')
def delete(id):
    aplicacionVacuna = AplicacionVacunas.query.get_or_404(id)

    db.session.delete(aplicacionVacuna)
    db.session.commit()

    return redirect(url_for('aplicacionvacuna.index'))