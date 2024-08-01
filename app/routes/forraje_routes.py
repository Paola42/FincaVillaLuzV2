from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.forrajes import Forrajes
from app import db

#   Rutas - Forraje
bp = Blueprint('forraje', __name__)


#   Index
@bp.route('/Forrajes')
def index():
    dataForrajes = Forrajes.query.all()

    return render_template('forrajes/index.html', dataForrajes=dataForrajes)


#   Add
@bp.route('/Forrajes/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        fechaDeSiembraForraje = request.form['fechaDeSiembraForraje']
        fechaDeCosechaForraje = request.form['fechaDeCosechaForraje']
        especieForraje = request.form['especieForraje']
        areaForraje = request.form['areaForraje']
        manejosForraje = request.form['manejosForraje']
        aforoForraje = request.form['aforoForraje']

        newForraje = Forrajes(fechaDeSiembraForraje=fechaDeSiembraForraje, fechaDeCosechaForraje=fechaDeCosechaForraje, especieForraje=especieForraje, areaForraje=areaForraje, manejosForraje=manejosForraje, aforoForraje=aforoForraje)
        db.session.add(newForraje)
        db.session.commit()

        return redirect(url_for('forraje.index'))
    
    return render_template('forrajes/add.html')


#   Edit
@bp.route('/Forrajes/edit/<int:idForraje>', methods=['GET', 'POST'])
def edit(idForraje):
    forraje = Forrajes.query.get_or_404(idForraje)

    if request.method == 'POST':
        forraje.fechaDeSiembraForraje = request.form['fechaDeSiembraForraje']
        forraje.fechaDeCosechaForraje = request.form['fechaDeCosechaForraje']
        forraje.especieForraje = request.form['especieForraje']
        forraje.areaForraje = request.form['areaForraje']
        forraje.manejosForraje = request.form['manejosForraje']
        forraje.aforoForraje = request.form['aforoForraje']

        db.session.commit()
        
        return redirect(url_for('forraje.index'))
    
    return render_template('forrajes/edit.html', forraje=forraje)


#   Delete
@bp.route('/Forrajes/delete/<int:idForraje>')
def delete(idForraje):
    forraje = Forrajes.query.get_or_404(idForraje)

    db.session.delete(forraje)
    db.session.commit()

    return redirect(url_for('forraje.index'))