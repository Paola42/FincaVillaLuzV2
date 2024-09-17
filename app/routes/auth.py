from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.administradores import Administrador
from app.models.aprendices import Aprendices
from app.models.instructores import Instructores
from app.models.usuarios import Usuarios
from app.models.operarios import Operarios

from app import db


auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/")
def index():
    return render_template('/principal/principal.html')


@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    
    
    if request.method == 'POST':
        # Recoger los datos del formulario
        nombre = request.form.get('nombre')
        documento = request.form.get('documento')
        direccion = request.form.get('direccion')
        telefono = request.form.get('telefono')
        correo = request.form.get('correo')
        password = request.form.get('password')
        tipo = request.form.get('tipo')
        flash(f'El usuario {tipo} ha sido registrado correctamente.', 'success')
        
        # Crear el usuario basado en el tipo
        if tipo == 'aprendiz':
            nuevo_usuario = Aprendices(
                nombreAprendiz=nombre, 
                documentoAprendiz=documento, 
                direccionAprendiz=direccion, 
                telefonoAprendiz=telefono, 
                correoAprendiz=correo, 
                passwordAprendiz=password
            )
        
        elif tipo == 'instructor':
            nuevo_usuario = Instructores(
                nombreInstructor=nombre, 
                documentoInstructor=documento, 
                direccionInstructor=direccion, 
                telefonoInstructor=telefono, 
                correoIntructor =correo, 
                PasswordInstructor=password
            )
        
        elif tipo == 'operario':
            nuevo_usuario = Operarios(
                nombreOperario=nombre, 
                documentoOperario=documento, 
                direccionOperario=direccion, 
                telefonoOperario=telefono, 
                correoOperario=correo, 
                passwordOperario=password
            )
        
        elif tipo == 'administrador':
            nuevo_usuario = Administrador(
                nombreAdministrador=nombre, 
                documentoAdministrador=documento, 
                direccionAdministrador=direccion, 
                telefonoAdministrador=telefono, 
                correoAdministrador=correo, 
                passwordAdministrador=password
            )
        
        else:
            return  "Tipo de usuario no válido", 400
        
        # Añadir y guardar en la base de datos
        db.session.add(nuevo_usuario)
        db.session.commit()
        # Redirigir a la vista de login
        return redirect(url_for('auth.principal'))

    return render_template("registro/registro.html")
    


#------------------------------------------------------------login----------------------------------


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo= request.form['correo']
        password = request.form['password']
       # busca el administrador con las credenciales proporcionadas
        administrador = Administrador.query.filter_by(correoAdministrador=correo, passwordAdministrador =password).first()
        
        if administrador:
            login_user(administrador)
            flash("Login successful!", "success")
            

            return render_template('bovinos/index.html')
    
        
        
        aprendiz = Aprendices.query.filter_by(correoAprendiz=correo, passwordAprendiz=password).first()
        
        if aprendiz:
            login_user(aprendiz)
            flash("Login successful!", "success")

            return render_template('inicio/index2.html')

        
        flash('Invalid credentials. Please try again.', 'danger')
        
        operario = Operarios.query.filter_by( correoOperario=correo, passwordOperario=password).first()
        
        if operario:
            login_user(operario)
            flash("Login successful!", "success")

            return render_template('inicio/index3.html')

        
        flash('Invalid credentials. Please try again.', 'danger')
    
        
        instructor= Instructores.query.filter_by(correo=correo, Password=password).first()
        
        if instructor:
            login_user(instructor)
            flash("Login successful!", "success")

            return render_template('inicio/index1.html')
        
        flash('Invalid credentials. Please try again.', 'danger')
    
    
    return render_template("login/login.html")

@auth_bp.route('/operario', methods=['GET', 'POST'])
def operario():
    return render_template('inicio/index3.html')



@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))


@auth_bp.route('/principal')
def principal():
    return render_template('principal/principal.html')



