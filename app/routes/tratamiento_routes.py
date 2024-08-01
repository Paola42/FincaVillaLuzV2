from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.tratamientos import Tratamientos
from app.models.medicamentos import Medicamentos
from app.models.vacunas import Vacunas
from app.models.eventos import Eventos
from app import db

#   Rutas - Tratamientos
bp = Blueprint('tratamiento', __name__)


#   Index
@bp.route('/Tratamientos')
def index():
    dataTratamientos = Tratamientos.query.all()
    dataMedicamentos = Medicamentos.query.all()
    dataVacunas = Vacunas.query.all()
    dataEventos = Eventos.query.all()

    return render_template('tratamientos/index.html', dataTratamientos=dataTratamientos, dataMedicamentos=dataMedicamentos, dataVacunas=dataVacunas, dataEventos=dataEventos)


#   Add
@bp.route('/Tratamientos/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        fechaInicioTratamiento = request.form['fechaInicioTratamiento']
        fechaFinTratamiento = request.form['fechaFinTratamiento']
        descripcionTratamiento = request.form['descripcionTratamiento']
        dosisTratamiento = request.form['dosisTratamiento']
        viaAdministracionTratamiento = request.form['viaAdministracionTratamiento']
        observacionesTratamiento = request.form['observacionesTratamiento']
        frecuenciaTratamiento = request.form['frecuenciaTratamiento']
        idMedicamento = request.form['idMedicamento']
        idVacuna = request.form['idVacuna']
        idEvento = request.form['idEvento']

        newTratamiento = Tratamientos(fechaInicioTratamiento=fechaInicioTratamiento, fechaFinTratamiento=fechaFinTratamiento, descripcionTratamiento=descripcionTratamiento,dosisTratamiento=dosisTratamiento, viaAdministracionTratamiento=viaAdministracionTratamiento, observacionesTratamiento=observacionesTratamiento, frecuenciaTratamiento=frecuenciaTratamiento, idMedicamento=idMedicamento, idVacuna=idVacuna, idEvento=idEvento)
        db.session.add(newTratamiento)
        db.session.commit()

        return redirect(url_for('tratamiento.index'))
    
    dataMedicamentos = Medicamentos.query.all()
    dataVacunas = Vacunas.query.all()
    dataEventos = Eventos.query.all()

    return render_template('tratamientos/add.html', dataMedicamentos=dataMedicamentos, dataVacunas=dataVacunas, dataEventos=dataEventos)


#   Edit
@bp.route('/Tratamientos/edit/<int:idTratamiento>', methods=['GET', 'POST'])
def edit(idTratamiento):
    tratamiento = Tratamientos.query.get_or_404(idTratamiento)

    if request.method == 'POST':
        tratamiento.fechaInicioTratamiento = request.form['fechaInicioTratamiento']
        tratamiento.fechaFinTratamiento = request.form['fechaFinTratamiento']
        tratamiento.descripcionTratamiento = request.form['descripcionTratamiento']
        tratamiento.dosisTratamiento = request.form['dosisTratamiento']
        tratamiento.viaAdministracionTratamiento = request.form['viaAdministracionTratamiento']
        tratamiento.observacionesTratamiento = request.form['observacionesTratamiento']
        tratamiento.frecuenciaTratamiento = request.form['frecuenciaTratamiento']
        tratamiento.idMedicamento = request.form['idMedicamento']
        tratamiento.idVacuna = request.form['idVacuna']
        tratamiento.idEvento = request.form['idEvento']

        db.session.commit()
        
        return redirect(url_for('tratamiento.index'))
    
    dataMedicamentos = Medicamentos.query.all()
    dataVacunas = Vacunas.query.all()
    dataEventos = Eventos.query.all()

    return render_template('tratamientos/edit.html', tratamiento=tratamiento, dataMedicamentos=dataMedicamentos, dataVacunas=dataVacunas, dataEventos=dataEventos)


#   Delete
@bp.route('/Tratamientos/delete/<int:idTratamiento>')
def delete(idTratamiento):
    tratamiento = Tratamientos.query.get_or_404(idTratamiento)

    db.session.delete(tratamiento)
    db.session.commit()

    return redirect(url_for('tratamiento.index'))
