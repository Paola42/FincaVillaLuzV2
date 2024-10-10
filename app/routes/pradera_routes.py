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

    return render_template('pradera/index.html', dataPraderas=dataPraderas, dataForrajes=dataForrajes)


#   Add
@bp.route('/Praderas/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombrePradera = request.form['nombrePradera']
        ubicacion = request.form['ubicacion']
        capacidadCarga = request.form['capacidadCarga']
        estadoDePastoreo = request.form['estadoDePastoreo']
        manejos = request.form['manejos']
        aforos = request.form['aforos']
        area = request.form['area']
        idForraje = request.form['idForraje']

        newPradera = Praderas( nombrePradera=nombrePradera,              
            ubicacion=ubicacion, 
            capacidadCarga=capacidadCarga, 
            estadoDePastoreo=estadoDePastoreo, 
            manejos=manejos, 
            aforos=aforos, 
            area=area, 
            idForraje=idForraje,
        )
        db.session.add(newPradera)
        db.session.commit()

        return redirect(url_for('pradera.index'))
    
    dataForrajes = Forrajes.query.all()
    pradera = Praderas.query.all()
    return render_template('Pradera/add.html', dataForrajes=dataForrajes, praderas=pradera)


#   Edit
@bp.route('/Praderas/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    pradera = Praderas.query.get_or_404(id)

    if request.method == 'POST':
        pradera.nombrePradera = request.form['nombrePradera']
        pradera.ubicacion = request.form['ubicacion']
        pradera.capacidadCarga = request.form['capacidadCarga']
        pradera.estadoDePastoreo = request.form['estadoDePastoreo']
        pradera.manejos = request.form['manejos']
        pradera.aforos = request.form['aforos']
        pradera.area= request.form['area']
        pradera.idForraje = request.form['idForraje']

        db.session.commit()
        
        return redirect(url_for('pradera.index'))
    
    dataForrajes = Forrajes.query.all()

    return render_template('pradera/edit.html', pradera=pradera, dataForrajes=dataForrajes)


#   Delete
@bp.route('/Praderas/delete/<int:id>')
def delete(id):
    pradera = Praderas.query.get_or_404(id)

    db.session.delete(pradera)
    db.session.commit()

    return redirect(url_for('pradera.index'))
