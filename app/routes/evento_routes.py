from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.eventos import Eventos
from app.models.animales import Animales
from app.models.enfermedades import Enfermedades
from app.models.instructores import Instructores
from app import db

#   Rutas - Eventos
bp = Blueprint('evento', __name__)


#   Index
@bp.route('/Eventos')
def index():
    dataEventos = Eventos.query.all()
    dataAnimales = Animales.query.all()
    dataEnfermedades = Enfermedades.query.all()
    dataInstructores = Instructores.query.all()

    return render_template('eventos/index.html', dataEventos=dataEventos, dataAnimales=dataAnimales, dataEnfermedades=dataEnfermedades, dataInstructores=dataInstructores)


#   Add
@bp.route('/Eventos/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        idAnimal = request.form['idAnimal']
        idEnfermedad = request.form['idEnfermedad']
        idInstructor = request.form['idInstructor']

        newEvento = Eventos(idAnimal=idAnimal, idEnfermedad=idEnfermedad, idInstructor=idInstructor)
        db.session.add(newEvento)
        db.session.commit()

        return redirect(url_for('evento.index'))
    
    dataAnimales = Animales.query.all()
    dataEnfermedades = Enfermedades.query.all()
    dataInstructores = Instructores.query.all()

    return render_template('eventos/index.html', dataAnimales=dataAnimales, dataEnfermedades=dataEnfermedades, dataInstructores=dataInstructores)

#   Edit
@bp.route('/Eventos/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    evento = Eventos.query.get_or_404(id)

    if request.method == 'POST':
        evento.idAnimal = request.form['idAnimal']
        evento.idEnfermedad = request.form['idEnfermedad']
        evento.idInstructor = request.form['idInstructor']

        db.session.commit()
        
        return redirect(url_for('evento.index'))
    
    dataAnimales = Animales.query.all()
    dataEnfermedades = Enfermedades.query.all()
    dataInstructores = Instructores.query.all()

    return render_template('eventos/index.html', evento=evento,dataAnimales=dataAnimales, dataEnfermedades=dataEnfermedades, dataInstructores=dataInstructores)

#   Delete
@bp.route('/Eventos/delete/<int:id>')
def delete(id):
    evento = Eventos.query.get_or_404(id)

    db.session.delete(evento)
    db.session.commit()

    return redirect(url_for('evento.index'))