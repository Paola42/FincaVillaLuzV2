from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.animalesMejorados import AnimalesMejorados
from app.models.animales import Animales
from app import db

#   Rutas - Animal mejorado
bp = Blueprint('animalmejorado', __name__)


#   Index
@bp.route('/animalmejorado')
def index():
    dataAnimalesMejorados = AnimalesMejorados.query.all()
    dataAnimales = Animales.query.all()

    return render_template('animalMejorado/index.html', dataAnimalesMejorados=dataAnimalesMejorados, dataAnimales=dataAnimales)

#   Add
@bp.route('/animalmejorado/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        idPadreAportante = request.form['idPadreAportante']
        nombrePadreAportante = request.form['nombrePadreAportante']
        razaPadreAportante = request.form['razaPadreAportante']
        idMadreAportante = request.form['idMadreAportante']
        nombreMadreAportante = request.form['nombreMadreAportante']
        razaMadreAportante = request.form['razaMadreAportante']
        idAnimal= request.form['idAnimal']

        newAnimalMejorado = AnimalesMejorados(idPadreAportante=idPadreAportante, nombrePadreAportante=nombrePadreAportante, razaPadreAportante=razaPadreAportante, idMadreAportante=idMadreAportante, nombreMadreAportante=nombreMadreAportante, razaMadreAportante=razaMadreAportante,idAnimal=idAnimal)
        db.session.add(newAnimalMejorado)
        db.session.commit()

        return redirect(url_for('animalmejorado.index'))
    
    dataAnimales = Animales.query.all()
     
    return render_template('animalMejorado/add.html', dataAnimales=dataAnimales)


#   Edit
@bp.route('/animalmejorado/edit/<int:idAnimalMejorado>', methods=['GET', 'POST'])
def edit(idAnimalMejorado):
    animalMejorado = AnimalesMejorados.query.get_or_404(idAnimalMejorado)

    if request.method == 'POST':
        animalMejorado.idPadreAportante = request.form['idPadreAportante']
        animalMejorado.nombrePadreAportante = request.form['nombrePadreAportante']
        animalMejorado.razaPadreAportante = request.form['razaPadreAportante']
        animalMejorado.idMadreAportante = request.form['idMadreAportante']
        animalMejorado.nombreMadreAportante = request.form['nombreMadreAportante']
        animalMejorado.razaMadreAportante = request.form['razaMadreAportante']
        animalMejorado.idAnimal= request.form['idAnimal']
        
        

        db.session.commit()
        
        return redirect(url_for('animalmejorado.index'))
    
    dataAnimales = Animales.query.all()
    
     
    return render_template('animalMejorado/edit.html', animalMejorado=animalMejorado, dataAnimales=dataAnimales)


#   Delete
@bp.route('/animalMejorado/delete/<int:idAnimalMejorado>')
def delete(idAnimalMejorado):
    animalMejorado = AnimalesMejorados.query.get_or_404(idAnimalMejorado)

    db.session.delete(animalMejorado)
    db.session.commit()

    return redirect(url_for('animalmejorado.index'))