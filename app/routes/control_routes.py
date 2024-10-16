from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.controles import Controles
from app.models.animalesMejorados import AnimalesMejorados
from app import db
from datetime import datetime


#   Rutas - Controles
bp = Blueprint('control', __name__)


#   Index
@bp.route('/Controles')
def index():
    dataControles = Controles.query.all()
    dataAnimalesMejorados = AnimalesMejorados.query.all()

    return render_template('control/index.html', dataControles=dataControles, dataAnimalesMejorados=dataAnimalesMejorados)


#   Add
@bp.route('/Controles/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        fecha = request.form['fecha']
        estado = request.form['estado']
        idAnimalMejorado = request.form['idAnimalMejorado']
        fecha = datetime.strptime(fecha, '%Y-%m-%d').date()

        newControl = Controles(descripcion=descripcion, fecha=fecha, estado=estado, animalMejorado=idAnimalMejorado)
        db.session.add(newControl)
        db.session.commit()

        return redirect(url_for('control.index'))
    
    animal = AnimalesMejorados.query.all()

    return render_template('control/add.html', animales=animal)


#   Edit
@bp.route('/Controles/edit/<int:idControl>', methods=['GET', 'POST'])
def edit(idControl):
    control = Controles.query.get_or_404(idControl)

    if request.method == 'POST':
        control.descripcion = request.form['descripcion']
        control.fecha = request.form['fecha']
        control.fecha = datetime.strptime(control.fecha, '%Y-%m-%d').date()
        control.estado = request.form['estado']
        control.idAnimalMejorado = request.form['idAnimalMejorado']

        db.session.commit()
        
        return redirect(url_for('control.index'))
    
    animal = AnimalesMejorados.query.all()

    return render_template('control/edit.html', control=control, animales=animal)


#   Delete
@bp.route('/Controles/delete/<int:idControl>')
def delete(idControl):
    control = Controles.query.get_or_404(idControl)

    db.session.delete(control)
    db.session.commit()

    return redirect(url_for('control.index'))
