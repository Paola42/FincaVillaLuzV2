from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.vacunas import Vacunas
from app import db

#   Rutas - Vacuna
bp = Blueprint('vacuna', __name__)


#   Index
@bp.route('/Vacunas')
def index():
    dataVacunas = Vacunas.query.all()

    return render_template('vacunas/index.html', dataVacunas=dataVacunas)


#   Add
@bp.route('/Vacunas/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombreVacuna = request.form['nombreVacuna']
        dosisVacuna = request.form['dosisVacuna']
        viaAdministracionVacuna = request.form['viaAdministracionVacuna']
        intervaloRevacunacionVacuna = request.form['intervaloRevacunacionVacuna']
        enfermedadObjetivoVacuna = request.form['enfermedadObjetivoVacuna']
        tipoVacuna = request.form['tipoVacuna']
        planNacionalVacuna = request.form['planNacionalVacuna']

        newVacuna = Vacunas(nombreVacuna=nombreVacuna, dosisVacuna=dosisVacuna, viaAdministracionVacuna=viaAdministracionVacuna, intervaloRevacunacionVacuna=intervaloRevacunacionVacuna, enfermedadObjetivoVacuna=enfermedadObjetivoVacuna, tipoVacuna=tipoVacuna, planNacionalVacuna=planNacionalVacuna)
        db.session.add(newVacuna)
        db.session.commit()

        return redirect(url_for('vacuna.index'))
    
    return render_template('vacunas/add.html')


#   Edit
@bp.route('/Vacunas/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    vacuna = Vacunas.query.get_or_404(id)

    if request.method == 'POST':
        vacuna.nombreVacuna = request.form['nombreVacuna']
        vacuna.dosisVacuna = request.form['dosisVacuna']
        vacuna.viaAdministracionVacuna = request.form['viaAdministracionVacuna']
        vacuna.intervaloRevacunacionVacuna = request.form['intervaloRevacunacionVacuna']
        vacuna.enfermedadObjetivoVacuna = request.form['enfermedadObjetivoVacuna']
        vacuna.tipoVacuna = request.form['tipoVacuna']
        vacuna.planNacionalVacuna = request.form['planNacionalVacuna']

        db.session.commit()
        
        return redirect(url_for('vacuna.index'))
    
    return render_template('vacunas/edit.html', vacuna=vacuna)


#   Delete
@bp.route('/Vacunas/delete/<int:id>')
def delete(id):
    vacuna = Vacunas.query.get_or_404(id)

    db.session.delete(vacuna)
    db.session.commit()

    return redirect(url_for('vacuna.index'))
