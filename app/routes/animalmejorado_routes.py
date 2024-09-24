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

    return render_template('animalMejorado/index.html', dataAnimalesMejorados=dataAnimalesMejorados, dataAnimales=dataAnimales)


#   Add
@bp.route('/AnimalesMejorados/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        idPadreAportante = request.form['idPadreAportante']
        nombrePadreAportante = request.form['nombrePadre']
        razaPadreAportante = request.form['razaPadreAportante']
        idMadreAportante = request.form['idMadreAportante']
        nombreMadreAportante = request.form['nombreMadreAportante']
        razaMadreAportante = request.form['razaMadreAportante']
        animal = request.form['idAnimal']

        newAnimalMejorado = AnimalesMejorados(idPadreAportante=idPadreAportante, nombrePadreAportante=nombrePadreAportante, razaPadreAportante=razaPadreAportante, idMadreAportante=idMadreAportante, nombreMadreAportante=nombreMadreAportante, razaMadreAportante=razaMadreAportante, animal=animal)
        db.session.add(newAnimalMejorado)
        db.session.commit()

        return redirect(url_for('animalmejorado.index'))
    
    dataAnimales = Animales.query.all()
     
    return render_template('animalMejorado/add.html', dataAnimales=dataAnimales)


#   Edit
@bp.route('/AnimalesMejorados/edit/<int:idAnimalMejorado>', methods=['GET', 'POST'])
def edit(idAnimalMejorado):
    animalMejorado = AnimalesMejorados.query.get_or_404(idAnimalMejorado)

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
     
    return render_template('animalMejorado/add.html', animalMejorado=animalMejorado, dataAnimales=dataAnimales, dataMejoramientosGeneticos=dataMejoramientosGeneticos)


#   Delete
@bp.route('/AnimalesMejorados/delete/<int:idAnimalMejorado>')
def delete(idAnimalMejorado):
    animalMejorado = AnimalesMejorados.query.get_or_404(idAnimalMejorado)

    db.session.delete(animalMejorado)
    db.session.commit()

    return redirect(url_for('animalmejorado.index'))