from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.tratamientos import Tratamientos
from app.models.medicamentos import Medicamentos
from app.models.vacunas import Vacunas
from app.models.eventos import Eventos
from app import db
from datetime import datetime

#   Rutas - Tratamientos
bp = Blueprint('tratamiento', __name__)


#   Index
@bp.route('/Tratamientos')
def index():
    tratamiento = Tratamientos.query.all()
    return render_template('tratamiento/index.html', tratamientos=tratamiento)


#   Add
@bp.route('/Tratamientos/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        fechaInicioTratamiento= request.form['fechaInicioTratamiento']
        fechaInicioTratamiento = datetime.strptime(fechaInicioTratamiento, '%Y-%m-%d').date()
        fechaFinTratamiento = request.form['fechaFinTratamiento']
        fechaFinTratamiento = datetime.strptime(fechaFinTratamiento, '%Y-%m-%d').date()
        descripcionTratamiento = request.form['descripcionTratamiento']
        dosis = request.form['dosis']
        viaAdministracion = request.form['viaAdministracion']
        observaciones = request.form['observaciones']
        frecuencia = request.form['frecuencia']
        idMedicamento = request.form['idMedicamento']
        idVacuna = request.form['idVacuna']
        idEvento = request.form['idEvento']
        newTratamiento = Tratamientos(fechaInicioTratamiento=fechaInicioTratamiento, 
                                      fechaFinTratamiento=fechaFinTratamiento, 
                                      descripcionTratamiento=descripcionTratamiento,
                                      dosis=dosis, 
                                      viaAdministracion=viaAdministracion, 
                                      observaciones=observaciones, 
                                      frecuencia=frecuencia, 
                                      idMedicamento=idMedicamento, idVacuna=idVacuna, 
                                      idEvento=idEvento)
        db.session.add(newTratamiento)
        db.session.commit()

        return redirect(url_for('tratamiento.index'))
    
    vacuna = Vacunas.query.all()
    medicamento= Medicamentos.query.all()
    evento= Eventos.query.all()
    
    return render_template('tratamiento/add.html',vacunas=vacuna,medicamentos=medicamento,eventos=evento)


#   Edit
@bp.route('/Tratamientos/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    tratamiento = Tratamientos.query.get_or_404(id)
    if request.method == 'POST':
        tratamiento.fechaInicioTratamiento = request.form['fechaInicioTratamiento']
        tratamiento.fechaInicioTratamiento = datetime.strptime(tratamiento.fechaInicioTratamiento, '%Y-%m-%d').date()
        tratamiento.fechaFinTratamiento = request.form['fechaFinTratamiento']
        tratamiento.fechaFinTratamiento = datetime.strptime(tratamiento.fechaFinTratamiento, '%Y-%m-%d').date()
        tratamiento.descripcionTratamiento = request.form['descripcionTratamiento']
        tratamiento.dosis = request.form['dosis']
        tratamiento.viaAdministracion = request.form['viaAdministracion']
        tratamiento.observaciones = request.form['observaciones']
        tratamiento.frecuencia = request.form['frecuencia']
        tratamiento.idMedicamento = request.form['idMedicamento']
        tratamiento.idVacuna = request.form['idVacuna']
        tratamiento.idEvento = request.form['idEvento']
        db.session.commit()
        return redirect(url_for('tratamiento.index'))
    
    vacuna = Vacunas.query.all()
    medicamento= Medicamentos.query.all()
    evento= Eventos.query.all()

    return render_template('tratamiento/edit.html', vacunas=vacuna,medicamentos=medicamento,eventos=evento,tratamiento=tratamiento)


#   Delete
@bp.route('/Tratamientos/delete/<int:id>')
def delete(id):
    tratamiento = Tratamientos.query.get_or_404(id)

    db.session.delete(tratamiento)
    db.session.commit()

    return redirect(url_for('tratamiento.index'))
