from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.medicamentos import Medicamentos
from app import db

#   Rutas - Medicamento
bp = Blueprint('medicamento', __name__)


#   Index
@bp.route('/Medicamentos')
def index():
    medicamento = Medicamentos.query.all()

    return render_template('medicamento/index.html', medicamentos=medicamento)


#   Add
@bp.route('/Medicamentos/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombreMedicamento = request.form['nombreMedicamento']
        dosisMedicamento = request.form['dosis']
        viaAdministracionMedicamento = request.form['viaAdministracion']
        indicacionesMedicamento = request.form['indicaciones']
        contraindicacionesMedicamento = request.form['contraIndicaciones']

        newMedicamento = Medicamentos(nombreMedicamento=nombreMedicamento, dosis=dosisMedicamento, viaAdministracion=viaAdministracionMedicamento, indicaciones=indicacionesMedicamento, contraindicaciones=contraindicacionesMedicamento)
        db.session.add(newMedicamento)
        db.session.commit()

        return redirect(url_for('medicamento.index'))
    
    return render_template('medicamento/add.html')


#   Edit
@bp.route('/Medicamentos/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    medicamento = Medicamentos.query.get_or_404(id)

    if request.method == 'POST':
        medicamento.nombreMedicamento = request.form['nombreMedicamento']
        medicamento.dosis = request.form['dosis']
        medicamento.viaAdministracion = request.form['viaAdministracion']
        medicamento.indicaciones = request.form['indicaciones']
        medicamento.contraindicaciones = request.form['contraindicaciones']
        db.session.commit()
        
        return redirect(url_for('medicamento.index'))
    
    return render_template('medicamento/edit.html', medicamento=medicamento)


#   Delete
@bp.route('/Medicamentos/delete/<int:id>')
def delete(id):
    medicamento = Medicamentos.query.get_or_404(id)

    db.session.delete(medicamento)
    db.session.commit()

    return redirect(url_for('medicamento.index'))
