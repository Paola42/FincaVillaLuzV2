from flask import Blueprint, render_template, request, redirect, url_for
from app.models.praderaAnimal import PraderaAnimal
from app.models.praderas import Praderas
from app.models.animales import Animales
from app import db

bp = Blueprint('praderaAnimal', __name__)

@bp.route('/praderaAnimal')
def index():
    dataPraderaAnimal = PraderaAnimal.query.all()
    return render_template('praderaAnimal/index.html', dataPraderaAnimal=dataPraderaAnimal)

@bp.route('/praderaAnimal/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        idAnimal = request.form['idAnimal']
        idPradera = request.form['idPradera']
        cantidad = request.form['cantidad']

        nuevaPraderaAnimal = PraderaAnimal(idAnimal=idAnimal, idPradera=idPradera, cantidad=cantidad)
        db.session.add(nuevaPraderaAnimal)
        db.session.commit()

        return redirect(url_for('praderaAnimal.index'))
    animal = Animales.query.all()
    pradera = Praderas.query.all()
    return render_template('praderaAnimal/add.html', animales=animal, praderas=pradera)

@bp.route('/praderaAnimal/edit/<int:idPraderaAnimal>', methods=['GET', 'POST'])
def edit(idPraderaAnimal):
    praderaAnimal = PraderaAnimal.query.get_or_404(idPraderaAnimal)
    
    if request.method == 'POST':
        praderaAnimal.idAnimal = request.form['idAnimal']
        praderaAnimal.idPradera = request.form['idPradera']
        praderaAnimal.cantidad = request.form['cantidad']

        db.session.commit()
        return redirect(url_for('praderaAnimal.index'))
    
    animales = Animales.query.all()
    praderas = Praderas.query.all()
    
    return render_template('praderaAnimal/edit.html', praderaAnimal=praderaAnimal, animales=animales, praderas=praderas)

@bp.route('/praderaAnimal/delete/<int:idPraderaAnimal>', methods=['GET', 'POST'])
def delete(idPraderaAnimal):
    praderaAnimal = PraderaAnimal.query.get_or_404(idPraderaAnimal)
    db.session.delete(praderaAnimal)
    db.session.commit()
    return redirect(url_for('praderaAnimal.index'))



