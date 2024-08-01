from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.mejoramientosGeneticos import MejoramientosGeneticos
from app.models.animalesMejorados import AnimalesMejorados
from app import db

#   Rutas - Mejoramientos Genéticos
bp = Blueprint('mejoramientogenetico', __name__)


#   Index
@bp.route('/MejoramientosGeneticos')
def index():
    dataMejoramientosGeneticos = MejoramientosGeneticos.query.all()
    dataAnimalesMejorados = AnimalesMejorados.query.all()

    return render_template('mejoramientosgeneticos/index.html', dataMejoramientosGeneticos=dataMejoramientosGeneticos, dataAnimalesMejorados=dataAnimalesMejorados)


#   Add
@bp.route('/MejoramientosGeneticos/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        tecnicaEventoGenetico = request.form['tecnicaEventoGenetico']
        fechaEventoGenetico = request.form['fechaEventoGenetico']
        resultadosGenetico = request.form['resultadosGenetico']
        detallesGenetico = request.form['detallesGenetico']
        idAnimalMejorado = request.form['idAnimalMejorado']

        newMejoramientoGenetico = MejoramientosGeneticos(tecnicaEventoGenetico=tecnicaEventoGenetico, fechaEventoGenetico=fechaEventoGenetico, resultadosGenetico=resultadosGenetico, detallesGenetico=detallesGenetico, idAnimalMejorado=idAnimalMejorado)
        db.session.add(newMejoramientoGenetico)
        db.session.commit()

        return redirect(url_for('mejoramientogenetico.index'))
    
    dataAnimalesMejorados = AnimalesMejorados.query.all()

    return render_template('mejoramientosgeneticos/add.html', dataAnimalesMejorados=dataAnimalesMejorados)


#   Edit
@bp.route('/MejoramientosGeneticos/edit/<int:idMejoramientoGenetico>', methods=['GET', 'POST'])
def edit(idMejoramientoGenetico):
    mejoramientoGenetico = MejoramientosGeneticos.query.get_or_404(idMejoramientoGenetico)

    if request.method == 'POST':
        mejoramientoGenetico.tecnicaEventoGenetico = request.form['tecnicaEventoGenetico']
        mejoramientoGenetico.fechaEventoGenetico = request.form['fechaEventoGenetico']
        mejoramientoGenetico.resultadosGenetico = request.form['resultadosGenetico']
        mejoramientoGenetico.detallesGenetico = request.form['detallesGenetico']
        mejoramientoGenetico.idAnimalMejorado = request.form['idAnimalMejorado']

        db.session.commit()
        
        return redirect(url_for('mejoramientogenetico.index'))
    
    dataAnimalesMejorados = AnimalesMejorados.query.all()

    return render_template('mejoramientosgeneticos/edit.html', mejoramientoGenetico=mejoramientoGenetico, dataAnimalesMejorados=dataAnimalesMejorados)


#   Delete
@bp.route('/MejoramientosGeneticos/delete/<int:idMejoramientoGenetico>')
def delete(idMejoramientoGenetico):
    mejoramientoGenetico = MejoramientosGeneticos.query.get_or_404(idMejoramientoGenetico)

    db.session.delete(mejoramientoGenetico)
    db.session.commit()

    return redirect(url_for('mejoramientogenetico.index'))
