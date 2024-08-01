from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.praderas import Praderas
from app.models.forrajes import Forrajes
from app import db

#   Rutas - Praderas
bp = Blueprint('pradera', __name__)


#   Index
@bp.route('/Praderas')
def index():
    dataPraderas = Praderas.query.all()
    dataForrajes = Forrajes.query.all()

    return render_template('praderas/index.html', dataPraderas=dataPraderas, dataForrajes=dataForrajes)


#   Add
@bp.route('/Praderas/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombrePradera = request.form['nombrePradera']
        ubicacionPradera = request.form['ubicacionPradera']
        capacidadCargaPradera = request.form['capacidadCargaPradera']
        estadoDePastoreoPradera = request.form['estadoDePastoreoPradera']
        manejosPradera = request.form['manejosPradera']
        aforosPradera = request.form['aforosPradera']
        areaPradera = request.form['areaPradera']
        idForraje = request.form['idForraje']

        newPradera = Praderas(nombrePradera=nombrePradera, ubicacionPradera=ubicacionPradera, capacidadCargaPradera=capacidadCargaPradera, estadoDePastoreoPradera=estadoDePastoreoPradera, manejosPradera=manejosPradera, aforosPradera=aforosPradera, areaPradera=areaPradera, idForraje=idForraje)
        db.session.add(newPradera)
        db.session.commit()

        return redirect(url_for('pradera.index'))
    
    dataForrajes = Forrajes.query.all()

    return render_template('praderas/add.html', dataForrajes=dataForrajes)


#   Edit
@bp.route('/Praderas/edit/<int:idPradera>', methods=['GET', 'POST'])
def edit(idPradera):
    pradera = Praderas.query.get_or_404(idPradera)

    if request.method == 'POST':
        pradera.nombrePradera = request.form['nombrePradera']
        pradera.ubicacionPradera = request.form['ubicacionPradera']
        pradera.capacidadCargaPradera = request.form['capacidadCargaPradera']
        pradera.estadoDePastoreoPradera = request.form['estadoDePastoreoPradera']
        pradera.manejosPradera = request.form['manejosPradera']
        pradera.aforosPradera = request.form['aforosPradera']
        pradera.areaPradera = request.form['areaPradera']
        pradera.idForraje = request.form['idForraje']

        db.session.commit()
        
        return redirect(url_for('pradera.index'))
    
    dataForrajes = Forrajes.query.all()

    return render_template('praderas/edit.html', pradera=pradera, dataForrajes=dataForrajes)


#   Delete
@bp.route('/Praderas/delete/<int:idPradera>')
def delete(idPradera):
    pradera = Praderas.query.get_or_404(idPradera)

    db.session.delete(pradera)
    db.session.commit()

    return redirect(url_for('pradera.index'))
