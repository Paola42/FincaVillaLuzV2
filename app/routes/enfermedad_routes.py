from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.enfermedades import Enfermedades
from app import db

#   Rutas - Enfermedad
bp = Blueprint('enfermedad', __name__)


#   Index
@bp.route('/Enfermedades')
def index():
    dataEnfermedades = Enfermedades.query.all()

    return render_template('enfermedad/index.html', dataEnfermedades=dataEnfermedades)


#   Add
@bp.route('/Enfermedades/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombreEnfermedad = request.form['nombreEnfermedad']
        sintomasEnfermedad = request.form['sintomasEnfermedad']
        detallesAdicionalesEnfermedad = request.form['detallesAdicionalesEnfermedad']

        newEnfermedad = Enfermedades(nombreEnfermedad=nombreEnfermedad, sintomasEnfermedad=sintomasEnfermedad, detallesAdicionalesEnfermedad=detallesAdicionalesEnfermedad)
        db.session.add(newEnfermedad)
        db.session.commit()

        return redirect(url_for('enfermedad.index'))
    
    return render_template('enfermedades/add.html')


#   Edit
@bp.route('/Enfermedades/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    enfermedad = Enfermedades.query.get_or_404(id)

    if request.method == 'POST':
        enfermedad.nombreEnfermedad = request.form['nombreEnfermedad']
        enfermedad.sintomasEnfermedad = request.form['sintomasEnfermedad']
        enfermedad.detallesAdicionalesEnfermedad = request.form['detallesAdicionalesEnfermedad']

        db.session.commit()
        
        return redirect(url_for('enfermedad.index'))
    
    return render_template('enfermedades/edit.html', enfermedad=enfermedad)


#   Delete
@bp.route('/Enfermedades/delete/<int:id>')
def delete(id):
    enfermedad = Enfermedades.query.get_or_404(id)

    db.session.delete(enfermedad)
    db.session.commit()

    return redirect(url_for('enfermedad.index'))