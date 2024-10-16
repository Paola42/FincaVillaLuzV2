from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.instructores import Instructores
from app import db

bp = Blueprint('instructor' ,__name__)
 
@bp.route('/Instructores')
def index():
    data = Instructores.query.all()
    return render_template('instructor/index.html', data=data)

@bp.route('/Instructores/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombreInstructor   = request.form['nombreInstructor']
        documentoInstructor  = request.form['documentoInstructor']
        direccionInstructor  = request.form['direccionInstructor']
        telefonoInstructor   = request.form['telefonoInstructor']
        correoInstructor     = request.form['correoInstructor']
        PasswordInstructor   = request.form['passwordInstructor']
        
        new_instructor= Instructores(nombreInstructor=nombreInstructor,  
                                     documentoInstructor= documentoInstructor, 
                                     direccionInstructor=direccionInstructor, 
                                     telefonoInstructor=telefonoInstructor, 
                                     correoInstructor=correoInstructor, 
                                     passwordInstructor=PasswordInstructor)
        db.session.add(new_instructor)
        db.session.commit()
        
        return redirect(url_for('instructor.index'))

    return render_template('instructor/add.html')

@bp.route('/instructor/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    instructor = Instructores.query.get_or_404(id)

    if request.method == 'POST':
        instructor.nombreInstructor     = request.form['nombreInstructor']
        instructor.documentoInstructor  = request.form['documentoInstructor']
        instructor.direccionInstructor  = request.form['direccionInstructor']
        instructor.telefonoInstructor   = request.form['telefonoInstructor']
        instructor.correoInstructor     = request.form['correoInstructor']
        instructor.passwordInstructor   = request.form['passwordInstructor']
        
    
        db.session.commit()
        return redirect(url_for('instructor.index'))

    return render_template('instructor/edit.html',instructor=instructor)
    

@bp.route('/instructor/delete/<int:id>')
def delete(id):
    instructor = Instructores.query.get_or_404(id)
    
    db.session.delete(instructor)
    db.session.commit()

    return redirect(url_for('instructor.index'))
