from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.operarios import Operarios
from app import db

bp = Blueprint('operario', __name__)

@bp.route('/Operarios')
def index():
    data = Operarios.query.all()
    return render_template('operario/index.html', data=data)

@bp.route('/Operarios/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombreOperario     = request.form['nombreOperario']
        documentoOperario  = request.form['documentoOperario']
        direccionOperario  = request.form['direccionOperario']
        telefonoOperario   = request.form['telefonoOperario ']
        correoOperario     = request.form['correOperario']
        passwordOperario   = request.form['passwordOperario']
        new_operario = Operarios(nombreOperario =nombreOperario, documentoOperario=documentoOperario, direccionOperario=direccionOperario, telefonoOperario=telefonoOperario, correoOperario=correoOperario,passwordOperario=passwordOperario)
        db.session.add(new_operario)
        db.session.commit()
        
        return redirect(url_for('operario.index'))

    return render_template('operario/add.html')

@bp.route('/operario/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    operario = Operarios.query.get_or_404(id)

    if request.method == 'POST':
        operario.nombreOperario     = request.form['nombreOperario']
        operario.documentoOperario  = request.form['documentoOperario']
        operario.direccionOperario  = request.form['direccionOperario']
        operario.telefonoOperario   = request.form['telefonoOperario']
        operario.correoOperario     = request.form['correOperario']
        operario.passwordOperario   = request.form['passwordOperario']
        
    
        db.session.commit()
        return redirect(url_for('operario.index'))

    return render_template('operario/edit.html',operario=operario)
    

@bp.route('/operario/delete/<int:id>')
def delete(id):
    operario = Operarios.query.get_or_404(id)
    
    db.session.delete(operario)
    db.session.commit()

    return redirect(url_for('operario.index'))
