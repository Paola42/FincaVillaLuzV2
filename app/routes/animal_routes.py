from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.animales import Animales
from app import db

#   Rutas - Animal
bp = Blueprint('animal', __name__)


#   Index
@bp.route('/Animales')
def index():
    dataAnimales = Animales.query.all()

    return render_template('animal/index.html', dataAnimales=dataAnimales)


#   Add
@bp.route('/Animales/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        
        especieAnimal = request.form['especieAnimal']
        razaAnimal = request.form['razaAnimal']
        sexoAnimal = request.form['sexoAnimal']
        fechaNacimiento = request.form['fechaNacimiento']
        pesoAnimal = request.form['pesoAnimal']
        padres = request.form['padres']
        idAnimalPadre = request.form['idAnimalPadre']
        idAnimalMadre = request.form['idAnimalMadre']

        new_animal = Animales( especieAnimal=especieAnimal, razaAnimal=razaAnimal, sexoAnimal=sexoAnimal, fechaNacimiento=fechaNacimiento, pesoAnimal=pesoAnimal,idAnimalPadre=idAnimalPadre, idAnimalMadre=idAnimalMadre, padres=padres)
        db.session.add(new_animal)
        db.session.commit()

        return redirect(url_for('animal.index'))
    
    return render_template('animal/add.html')

       
#   Edit
@bp.route('/animal/edit/<int:idAnimal>', methods=['GET', 'POST'])
def edit(id):
    animal = Animales.query.get_or_404(id)

    if request.method == 'POST':
        
        animal.especieAnimal = request.form['especieAnimal']
        animal.razaAnimal = request.form['razaAnimal']
        animal.sexoAnimal = request.form['sexoAnimal']
        animal.fechaNacimiento = request.form['fechaNacimiento']
        animal.pesoAnimal = request.form['peso']
        animal.padres = request.form['padres']
        animal.idAnimalPadre = request.form['idAnimalPadre']
        animal.idAnimalMadre = request.form['idAnimalMadre']

        db.session.commit()
        
        return redirect(url_for('animal.index'))
    
    return render_template('animales/edit.html', animal=animal)


#   Delete
@bp.route('/animal/delete/<int:id>')
def delete(id):
    animal = Animales.query.get_or_404(id)

    db.session.delete(animal)
    db.session.commit()

    return redirect(url_for('animal.index'))


# ruta para animal
@bp.route('/animal')
def animal():
    
    return redirect(url_for('animal/index.html')) 
