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
    pastoreo = Pastoreos.query.all()
    dataPraderas = Praderas.query.all()
    dataAnimales = Animales.query.all()

    return render_template('pastoreo/index.html', Pastoreo=pastoreo, dataPraderas=dataPraderas, dataAnimales=dataAnimales)


#   Add
@bp.route('/Pastoreos/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        fechaInicioPastoreo = request.form['fechaInicioPastoreo']
        fechaFinPastoreo = request.form['fechaFinPastoreo']  # Asegúrate de que este campo existe en el formulario
        duracionPastoreo = request.form['duracionPastoreo']
        CargaAnimal = request.form['CargaAnimal']  # Asegúrate de que este campo es correcto
        horasDePastoreo = request.form['horasDePastoreo']
        idPradera = request.form['idPradera']

        newPastoreo = Pastoreos(fechaInicioPastoreo=fechaInicioPastoreo, 
                                fechaFinPastoreo=fechaFinPastoreo,
                                duracionPastoreo=duracionPastoreo, 
                                CargaAnimal=CargaAnimal, 
                                horasDePastoreo=horasDePastoreo, 
                                idPradera=idPradera, 
                                )
        db.session.add(newPastoreo)
        db.session.commit()

        return redirect(url_for('pastoreo.index'))
    pastoreo = Pastoreos.query.all()
    pradera = Praderas.query.all()
    
    return render_template('pastoreo/add.html', Pastoreo=pastoreo, praderas=pradera)


#   Edit
@bp.route('/Pastoreos/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    pastoreo = Pastoreos.query.get_or_404(id)

    if request.method == 'POST':
        pastoreo.fechaInicioPastoreo = request.form['fechaInicioPastoreo']
        pastoreo.fechaFinPastoreo = request.form['fechaFinPastoreo']
        pastoreo.duracionPastoreo = request.form['duracionPastoreo']
        pastoreo.CargaAnimal = request.form['CargaAnimal']
        pastoreo.horasDePastoreo = request.form['horasDePastoreo']
        pastoreo.idPradera = request.form['idPradera']
        db.session.commit()
        
        return redirect(url_for('pastoreo.index'))
    
    return render_template('pastoreo/edit.html', pastoreo=pastoreo)

#   Delete
@bp.route('/Pastoreos/delete/<int:id>')
def delete(id):
    pastoreo = Pastoreos.query.get_or_404(id)

    db.session.delete(pastoreo)
    db.session.commit()

    return redirect(url_for('pastoreo.index'))
