from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.administradores import Administrador
from app import db

bp = Blueprint('administrador' ,__name__)
 
@bp.route('/Administrador')
def index():
    data = Administrador.query.all()
    return render_template('administrador/index.html', data=data)

@bp.route('/Administrador/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombreAdministrador     = request.form['nombreAdministrador']
        documentoAdministrador  = request.form['documentoAdministrador']
        direccionAdministrador  = request.form['direccionAdministrador']
        telefonoAdministrador   = request.form['telefonoAdministrador']
        correoAdministrador     = request.form['correoAdministrador']

        passwordAdministrador   = request.form['passwordAdministrador']

        passwordAdministrador  =  request.form['passwordAdministrador']

        new_administrador = Administrador(nombreAdministrador=nombreAdministrador, documentoAdministrador=documentoAdministrador, direccionAdministrador=direccionAdministrador, telefonoAdministrador=telefonoAdministrador, correoAdministrador=correoAdministrador, passwordAdministrador=passwordAdministrador)
        db.session.add(new_administrador)
        db.session.commit()
        
        return redirect(url_for('administrador.index'))

    return render_template('administrador/add.html')
@bp.route('/administrador/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    administrador = Administrador.query.get_or_404(id)

    if request.method == 'POST':
        administrador.nombreAdministrador     = request.form['nombreAdministrador']
        administrador.documentoAdministrador  = request.form['documentoAdministrador']
        administrador.direccionAdministrador  = request.form['direccionAdministrador']
        administrador.telefonoAdministrador   = request.form['telefonoAdministrador']
        administrador.correoAdministrador     = request.form['correoAdministrador']
        administrador.passwordAdministrador   = request.form['passwordAdministrador']
        
    
        db.session.commit()
        return redirect(url_for('administrador.index'))

    return render_template('administrador/edit.html',administrador=administrador)
    

@bp.route('/administrador/delete/<int:id>')
def delete(id):
    administrador = Administrador.query.get_or_404(id)
    
    db.session.delete(administrador)
    db.session.commit()

    return redirect(url_for('administrador.index'))



