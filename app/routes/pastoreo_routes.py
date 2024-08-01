from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.pastoreos import Pastoreos
from app.models.praderas import Praderas
from app.models.animales import Animales
from app import db

#   Rutas - Pastoreos
bp = Blueprint('pastoreo', __name__)


#   Index
@bp.route('/Pastoreos')
def index():
    dataPastoreos = Pastoreos.query.all()
    dataPraderas = Praderas.query.all()
    dataAnimales = Animales.query.all()

    return render_template('pastoreos/index.html', dataPastoreos=dataPastoreos, dataPraderas=dataPraderas, dataAnimales=dataAnimales)


#   Add
@bp.route('/Pastoreos/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        fechaInicioPastoreo = request.form['fechaInicioPastoreo']
        fechaFinPastoreo = request.form['fechaFinPastoreo']
        duracionPastoreo = request.form['duracionPastoreo']
        cargaAnimalPastoreo = request.form['cargaAnimalPastoreo']
        horasDePastoreo = request.form['horasDePastoreo']
        idPradera = request.form['idPradera']
        idAnimal = request.form['idAnimal']

        newPastoreo = Pastoreos(fechaInicioPastoreo=fechaInicioPastoreo, fechaFinPastoreo=fechaFinPastoreo, duracionPastoreo=duracionPastoreo, cargaAnimalPastoreo=cargaAnimalPastoreo, horasDePastoreo=horasDePastoreo, idPradera=idPradera, idAnimal=idAnimal)
        db.session.add(newPastoreo)
        db.session.commit()

        return redirect(url_for('pastoreo.index'))
    
    dataPraderas = Praderas.query.all()
    dataAnimales = Animales.query.all()

    return render_template('pastoreos/add.html', dataPraderas=dataPraderas, dataAnimales=dataAnimales)


#   Edit
@bp.route('/Pastoreos/edit/<int:idPastoreo>', methods=['GET', 'POST'])
def edit(idPastoreo):
    pastoreo = Pastoreos.query.get_or_404(idPastoreo)

    if request.method == 'POST':
        pastoreo.fechaInicioPastoreo = request.form['fechaInicioPastoreo']
        pastoreo.fechaFinPastoreo = request.form['fechaFinPastoreo']
        pastoreo.duracionPastoreo = request.form['duracionPastoreo']
        pastoreo.cargaAnimalPastoreo = request.form['cargaAnimalPastoreo']
        pastoreo.horasDePastoreo = request.form['horasDePastoreo']
        pastoreo.idPradera = request.form['idPradera']
        pastoreo.idAnimal = request.form['idAnimal']

        db.session.commit()
        
        return redirect(url_for('pastoreo.index'))
    
    dataPraderas = Praderas.query.all()
    dataAnimales = Animales.query.all()

    return render_template('pastoreos/edit.html', pastoreo=pastoreo, dataPraderas=dataPraderas, dataAnimales=dataAnimales)


#   Delete
@bp.route('/Pastoreos/delete/<int:idPastoreo>')
def delete(idPastoreo):
    pastoreo = Pastoreos.query.get_or_404(idPastoreo)

    db.session.delete(pastoreo)
    db.session.commit()

    return redirect(url_for('pastoreo.index'))
