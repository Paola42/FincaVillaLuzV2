from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.vacunas import Vacunas
from app import db

#   Rutas - Vacuna
bp = Blueprint('vacuna', __name__)


#   Index
@bp.route('/Vacunas')
def index():
    dataVacunas = Vacunas.query.all()

    return render_template('vacuna/index.html', dataVacunas=dataVacunas)


#   Add
@bp.route('/Vacunas/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombreVacuna = request.form['nombreVacuna']
        dosis= request.form['dosis']
        viaAdministracion = request.form['viaAdministracion']
        intervaloReVacunacion = request.form['intervaloReVacunacion']
        enfermedadObjetivo = request.form['enfermedadObjetivo']
        tipoVacuna = request.form['tipoVacuna']
        planNacional = request.form['planNacional']

        newVacuna = Vacunas(nombreVacuna=nombreVacuna, dosis=dosis, viaAdministracion=viaAdministracion, intervaloReVacunacion=intervaloReVacunacion, enfermedadObjetivo=enfermedadObjetivo, tipoVacuna=tipoVacuna, planNacional=planNacional)
        db.session.add(newVacuna)
        db.session.commit()

        return redirect(url_for('vacuna.index'))
    
    return render_template('vacuna/add.html')


#   Edit
@bp.route('/vacuna/edit/<int:idVacuna>', methods=['GET', 'POST'])
def edit(idVacuna):
    vacuna = Vacunas.query.get_or_404(idVacuna)

    if request.method == 'POST':
        vacuna.nombreVacuna = request.form['nombreVacuna']
        vacuna.dosis = request.form['dosis']
        vacuna.viaAdministracion = request.form['viaAdministracion']
        vacuna.intervaloReVacunacion = request.form['intervaloReVacunacion']
        vacuna.enfermedadObjetivo = request.form['enfermedadObjetivo']
        vacuna.tipoVacuna = request.form['tipoVacuna']
        vacuna.planNacional = request.form['planNacional']

        db.session.commit()
        
        return redirect(url_for('vacuna.index'))
    
    return render_template('vacuna/edit.html', vacuna=vacuna)


#   Delete
@bp.route('/Vacunas/delete/<int:idVacuna>')
def delete(idVacuna):
    vacuna = Vacunas.query.get_or_404(idVacuna)

    db.session.delete(vacuna)
    db.session.commit()

    return redirect(url_for('vacuna.index'))
