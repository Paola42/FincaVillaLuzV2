from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.medicamentos import Medicamentos
from app import db

#   Rutas - Medicamento
bp = Blueprint('medicamento', __name__)


#   Index
@bp.route('/Medicamentos')
def index():
    dataMedicamentos = Medicamentos.query.all()

    return render_template('medicamento/index.html', dataMedicamentos=dataMedicamentos)


#   Add
@bp.route('/Medicamentos/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombreMedicamento = request.form['nombreMedicamento']
        dosisMedicamento = request.form['dosisMedicamento']
        viaAdministracionMedicamento = request.form['viaAdministracionMedicamento']
        indicacionesMedicamento = request.form['indicacionesMedicamento']
        contradiccionesMedicamento = request.form['contradiccionesMedicamento']

        newMedicamento = Medicamentos(nombreMedicamento=nombreMedicamento, dosisMedicamento=dosisMedicamento, viaAdministracionMedicamento=viaAdministracionMedicamento, indicacionesMedicamento=indicacionesMedicamento, contradiccionesMedicamento=contradiccionesMedicamento)
        db.session.add(newMedicamento)
        db.session.commit()

        return redirect(url_for('medicamento.index'))
    
    return render_template('medicamentos/add.html')


#   Edit
@bp.route('/Medicamentos/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    medicamento = Medicamentos.query.get_or_404(id)

    if request.method == 'POST':
        medicamento.nombreMedicamento = request.form['nombreMedicamento']
        medicamento.dosisMedicamento = request.form['dosisMedicamento']
        medicamento.viaAdministracionMedicamento = request.form['viaAdministracionMedicamento']
        medicamento.indicacionesMedicamento = request.form['indicacionesMedicamento']
        medicamento.contradiccionesMedicamento = request.form['contradiccionesMedicamento']

        db.session.commit()
        
        return redirect(url_for('medicamento.index'))
    
    return render_template('medicamentos/edit.html', medicamento=medicamento)


#   Delete
@bp.route('/Medicamentos/delete/<int:id>')
def delete(id):
    medicamento = Medicamentos.query.get_or_404(id)

    db.session.delete(medicamento)
    db.session.commit()

    return redirect(url_for('medicamento.index'))
