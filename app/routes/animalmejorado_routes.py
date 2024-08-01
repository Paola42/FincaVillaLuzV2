from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.animalesMejorados import AnimalesMejorados
from app.models.animales import Animales
from app.models.mejoramientosGeneticos import MejoramientosGeneticos
from app import db

#   Rutas - Animal mejorado
bp = Blueprint('animalmejorado', __name__)


#   Index
@bp.route('/AnimalesMejorados')
def index():
    dataAnimalesMejorados = AnimalesMejorados.query.all()
    dataAnimales = Animales.query.all()
    dataMejoramientosGeneticos = MejoramientosGeneticos.query.all()

    return render_template('animalesmejorados/index.html', dataAnimalesMejorados=dataAnimalesMejorados, dataAnimales=dataAnimales, dataMejoramientosGeneticos=dataMejoramientosGeneticos)


#   Add
@bp.route('/AnimalesMejorados/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        idPadre = request.form['idPadre']
        idMadre = request.form['idMadre']
        idMejoramiento = request.form['idMejoramiento']
        idPadreAportante = request.form['idPadreAportante']
        nombrePadre = request.form['nombrePadre']
        razaPadre = request.form['razaPadre']
        nombreMadre = request.form['nombreMadre']
        razaMadre = request.form['razaMadre']

        newAnimalMejorado = AnimalesMejorados(idPadre=idPadre, idMadre=idMadre, idMejoramiento=idMejoramiento, idPadreAportante=idPadreAportante, nombrePadre=nombrePadre, razaPadre=razaPadre, nombreMadre=nombreMadre, razaMadre=razaMadre)
        db.session.add(newAnimalMejorado)
        db.session.commit()

        return redirect(url_for('animalmejorado.index'))
    
    dataAnimales = Animales.query.all()
    dataMejoramientosGeneticos = MejoramientosGeneticos.query.all()
     
    return render_template('animalesmejorados/add.html', dataAnimales=dataAnimales, dataMejoramientosGeneticos=dataMejoramientosGeneticos)


#   Edit
@bp.route('/AnimalesMejorados/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    animalMejorado = AnimalesMejorados.query.get_or_404(id)

    if request.method == 'POST':
        animalMejorado.idPadre = request.form['idPadre']
        animalMejorado.idMadre = request.form['idMadre']
        animalMejorado.idMejoramiento = request.form['idMejoramiento']
        animalMejorado.idPadreAportante = request.form['idPadreAportante']
        animalMejorado.nombrePadre = request.form['nombrePadre']
        animalMejorado.razaPadre = request.form['razaPadre']
        animalMejorado.nombreMadre = request.form['nombreMadre']
        animalMejorado.razaMadre = request.form['razaMadre']

        db.session.commit()
        
        return redirect(url_for('animalmejorado.index'))
    
    dataAnimales = Animales.query.all()
    dataMejoramientosGeneticos = MejoramientosGeneticos.query.all()
     
    return render_template('animalesmejorados/add.html', animalMejorado=animalMejorado, dataAnimales=dataAnimales, dataMejoramientosGeneticos=dataMejoramientosGeneticos)


#   Delete
@bp.route('/AnimalesMejorados/delete/<int:id>')
def delete(id):
    animalMejorado = AnimalesMejorados.query.get_or_404(id)

    db.session.delete(animalMejorado)
    db.session.commit()

    return redirect(url_for('animalmejorado.index'))