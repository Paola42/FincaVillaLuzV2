from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.aprendices import Aprendices
from app import db

bp = Blueprint('aprendiz', __name__)

@bp.route('/Aprendices')
def index():
    data = Aprendices.query.all()
    return render_template('aprendiz/index.html', data=data)

@bp.route('/aprendiz/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombreAprendiz     = request.form['nombreAprendiz']
        documentoAprendiz  = request.form['documentoAprendiz']
        direccionAprendiz  = request.form['direccionAprendiz']
        telefonoAprendiz   = request.form['telefonoAprendiz']
        correoAprendiz     = request.form['correoAprendiz']
        passwordAprendiz   = request.form['passwordAprendiz']
        new_aprendiz = Aprendices(nombreAprendiz =nombreAprendiz , documentoAprendiz=documentoAprendiz, direccionAprendiz=direccionAprendiz, telefonoAprendiz=telefonoAprendiz, correoAprendiz=correoAprendiz, passwordAprendiz=passwordAprendiz)
        db.session.add(new_aprendiz)
        db.session.commit()
        
        return redirect(url_for('aprendiz.index'))

    return render_template('aprendiz/add.html')

@bp.route('/aprendiz/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    aprendiz = Aprendices.query.get_or_404(id)

    if request.method == 'POST':
        aprendiz.nombreAprendiz     = request.form['nombreAprendiz']
        aprendiz.documentoAprendiz  = request.form['documentoAprendiz']
        aprendiz.direccionAprendiz  = request.form['direccionAprendiz']
        aprendiz.telefonoAprendiz   = request.form['telefonoAprendiz']
        aprendiz.correoAprendiz     = request.form['correoAprendiz']
        aprendiz.passwordAprendiz   = request.form['passwordAprendiz']
        
    
        db.session.commit()
        return redirect(url_for('aprendiz.index'))

    return render_template('aprendiz/edit.html',aprendiz=aprendiz)
    

@bp.route('/aprendiz/delete/<int:id>')
def delete(id):
    aprendiz = Aprendices.query.get_or_404(id)
    
    db.session.delete(aprendiz)
    db.session.commit()

    return redirect(url_for('aprendiz.index'))
