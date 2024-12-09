from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.mejoramientosGeneticos import MejoramientosGeneticos
from app.models.animalesMejorados import AnimalesMejorados
from app.models.animales import Animales
from app import db
from datetime import datetime
#   Rutas - Mejoramientos Genéticos
bp = Blueprint('mejoramientogenetico', __name__)


#   Index
@bp.route('/MejoramientosGeneticos')
def index():
    dataMejoramientosGeneticos = MejoramientosGeneticos.query.all()
    dataAnimalesMejorados = AnimalesMejorados.query.all()

    return render_template('mejoramientoGenetico/index.html', dataMejoramientosGeneticos=dataMejoramientosGeneticos, dataAnimalesMejorados=dataAnimalesMejorados)


#   Add
@bp.route('/MejoramientosGeneticos/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        tecnicaEventoGenetico = request.form['tecnicaEventoGenetico']
        fechaEvento = request.form['fechaEvento']
        fechaEvento = datetime.strptime(fechaEvento, '%Y-%m-%d').date()
        resultados = request.form['resultados']
        detalles = request.form['detalles']
        animalMejorado = request.form['animalMejorado']

        newMejoramientoGenetico = MejoramientosGeneticos(tecnicaEventoGenetico=tecnicaEventoGenetico, fechaEvento=fechaEvento, resultados=resultados, detalles=detalles, animalMejorado=animalMejorado)
        db.session.add(newMejoramientoGenetico)
        db.session.commit()
        return redirect(url_for('mejoramientogenetico.index'))
    
    animal = AnimalesMejorados.query.all()
   

    return render_template('mejoramientogenetico/add.html', animales=animal)


#   Edit
@bp.route('/MejoramientosGeneticos/edit/<int:idMejoramientoGenetico>', methods=['GET', 'POST'])
def edit(idMejoramientoGenetico):
    mejoramientoGenetico = MejoramientosGeneticos.query.get_or_404(idMejoramientoGenetico)

    if request.method == 'POST':
        
        mejoramientoGenetico.tecnicaEventoGenetico = request.form['tecnicaEventoGenetico']
        mejoramientoGenetico.fechaEvento = request.form['fechaEvento']
        mejoramientoGenetico.fechaEvento = datetime.strptime(mejoramientoGenetico.fechaEvento, '%Y-%m-%d').date()
        mejoramientoGenetico.resultados = request.form['resultados']
        mejoramientoGenetico.detalles = request.form['detalles']
        mejoramientoGenetico.animalMejorado = request.form['animalMejorado']

        db.session.commit()
        
        return redirect(url_for('mejoramientogenetico.index'))
    
    animal = AnimalesMejorados.query.all()

    return render_template('mejoramientogenetico/edit.html', mejoramientoGenetico=mejoramientoGenetico, animales=animal)


#   Delete
@bp.route('/MejoramientosGeneticos/delete/<int:idMejoramientoGenetico>')
def delete(idMejoramientoGenetico):
    mejoramientoGenetico = MejoramientosGeneticos.query.get_or_404(idMejoramientoGenetico)

    db.session.delete(mejoramientoGenetico)
    db.session.commit()

    return redirect(url_for('mejoramientogenetico.index'))
