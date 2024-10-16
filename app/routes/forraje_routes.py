from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.forrajes import Forrajes
from app import db
from datetime import datetime

#   Rutas - Forraje
bp = Blueprint('forraje', __name__)


#   Index
@bp.route('/Forraje')
def index():
    dataForrajes = Forrajes.query.all()

    return render_template('forraje/index.html', dataForrajes=dataForrajes)


#   Add
@bp.route('/forraje/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        especieForraje = request.form['especieForraje']
        fechaDeSiembraForraje = request.form['fechaDeSiembraForraje']
        fechaDeSiembraForraje = datetime.strptime(fechaDeSiembraForraje, '%Y-%m-%d').date()
        fechaDeCosechaForraje = request.form['fechaDeCosechaForraje']
        fechaDeSiembraForraje = datetime.strptime(fechaDeSiembraForraje, '%Y-%m-%d').date()
        areaForraje = request.form['areaForraje']
        manejosForraje = request.form['manejosForraje']
        aforoForraje = request.form['aforoForraje']

        newForraje = Forrajes(especieForraje=especieForraje,fechaDeSiembraForraje=fechaDeSiembraForraje, fechaDeCosechaForraje=fechaDeCosechaForraje,  areaForraje=areaForraje, manejosForraje=manejosForraje, aforoForraje=aforoForraje)
        db.session.add(newForraje)
        db.session.commit()

        return redirect(url_for('forraje.index'))
    
    return render_template('forraje/add.html')


#   Edit
@bp.route('/forraje/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    forraje = Forrajes.query.get_or_404(id)

    if request.method == 'POST':
        forraje.areaForraje = request.form['areaForraje']
        forraje.fechaDeSiembraForraje = request.form['fechaDeSiembraForraje']
        forraje.fechaDeSiembraForraje = datetime.strptime(forraje.fechaDeSiembraForraje, '%Y-%m-%d').date()
        forraje.fechaDeCosechaForraje = request.form['fechaDeCosechaForraje']
        forraje.fechaDeSiembraForraje = datetime.strptime(forraje.fechaDeSiembraForraje, '%Y-%m-%d').date()
        forraje.especieForraje = request.form['especieForraje']
        forraje.manejosForraje = request.form['manejosForraje']
        forraje.aforoForraje = request.form['aforoForraje']

        db.session.commit()
        
        return redirect(url_for('forraje.index'))
    
    return render_template('forraje/edit.html', forraje=forraje)


#   Delete
@bp.route('/forraje/delete/<int:id>')
def delete(id):
    forraje = Forrajes.query.get_or_404(id)

    db.session.delete(forraje)
    db.session.commit()

    return redirect(url_for('forraje.index'))
