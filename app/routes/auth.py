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
    return render_template('principal/principal.html')


@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Procesar el formulario de registro
        nombre = request.form['nombre']
        documento = request.form['documento']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        correo = request.form['correo']
        password = request.form['password']
        tipo    = request.form['tipo']

        
        if tipo == "instructor":
            nombre=nombre, 
            documento=documento, 
            direccion=direccion, 
            telefono=telefono, 
            correo=correo, 
            password=password

        nuevo_usuario = Usuarios(
            nombre=nombre, 
            documento=documento, 
            direccion=direccion, 
            telefono=telefono, 
            correo=correo, 
            password=password, 
            tipo=tipo
        )
        try:
            db.session.add(nuevo_usuario)
            db.session.commit()
            flash('Registro exitoso!', 'success')

            # Redirigir según el tipo de usuario
            if tipo == 'aprendiz':
                return redirect(url_for('templates_aprendiz'))
            elif tipo == 'instructor':
                return redirect(url_for('formulario_instructor'))
            elif tipo == 'administrador':
                return redirect(url_for('formulario_administrador'))
            else:
                flash('Tipo de usuario no válido.','danger')

        except:
            flash('Error en el registro. Por favor, intente de nuevo.', 'danger')

    return render_template('registro/registro.html')


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







