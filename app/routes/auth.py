from flask import Blueprint, render_template, redirect, url_for, request, flash, Flask  
from flask_login import login_user, logout_user, login_required 
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
from app.models.administradores import Administrador
from app.models.aprendices import Aprendices
from app.models.instructores import Instructores
from app.models.usuarios import Usuarios
from app.models.operarios import Operarios
from app.models.animales import Animales
from app import db
import os
#-------------------------------------------------------------emails---------------------------------------------
app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'
mail = Mail(app)
s = URLSafeTimedSerializer(app.secret_key)
#--------------------------------------------------------------------emails---------------------------------------------------------

auth_bp = Blueprint('auth', __name__)


@auth_bp.route("/")
def index():
    return render_template("principal/principal.html")


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
                correoInstructor =correo, 
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
            

            return render_template('inicio/index.html')
    
        
        
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
    
        
        instructor= Instructores.query.filter_by(correoInstructor=correo, PasswordInstructor=password).first()
        
        if instructor:
            login_user(instructor)
            flash("Login successful!", "success")

            return render_template('inicio/index2.html')
        
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

@auth_bp.route('/evento')
def evento():
    return render_template('eventos/index.html')


@auth_bp.route('/principal')
def principal():
    return render_template('principal/principal.html')

@auth_bp.route('/principal2')
def principal2():
    
    return render_template('/recuperacion.html')



#-----------------------------------------------------recuperacion de contraseña por gmail---------------------------------------------------



@auth_bp.route('/restablecer_contraseña')
def restablecer_contraseña():
    
    return render_template('principal/recuperar_Contraseña.html')

@auth_bp.route('/recuperacion')
def recuperacion():
    
    return render_template('principal/contraseñas.html')



@auth_bp.route('/solicitar_restablecimiento', methods=['POST'])
def solicitar_restablecimiento():
    email = request.form['email']
    token = s.dumps(email, salt='email-reset-salt')
    link = url_for('auth.recuperacion', token=token, _external=True)

    msg = Message('usted ha solicitado la recuperación de su contraseña', sender='juanespitia538@gmail.com', recipients=['email'])
    msg.body = f'Para restablecer tu contraseña, haz clic en el siguiente enlace: {link}'
    
    try:
        mail.send(msg)
        flash('Se ha enviado un correo con instrucciones para restablecer tu contraseña.', 'success')
    except Exception as e:
        flash(f'Error al enviar el correo: {str(e)}', 'error')

    return redirect(url_for('auth.restablecer_contraseña'))


@auth_bp.route('/restablecer_contraseña/<token>', methods=['GET', 'POST'])
def restablecer_contrasena(token):
    if request.method == 'POST':
            password = request.form['password']
            confirm_password = request.form['confirm_password']
        
        # Aquí deberías validar que las contraseñas coincidan y actualizar la contraseña en la base de datos
            if password != confirm_password:
                flash('Las contraseñas no coinciden.', 'error')
                return redirect(url_for('auth.restablecer_contraseña', token=token))
        
            flash('Tu contraseña ha sido restablecida con éxito.', 'success')
            return redirect(url_for('auth.login'))

    try:
        email = s.loads(token, salt='email-reset-salt', max_age=3600)  # Token válido por 1 hora
    except Exception:
        flash('El enlace es inválido o ha expirado.', 'error')
        return redirect(url_for('auth.restablecer_contraseña'))

    return render_template('restablecer_contrasena.html', token=token)

#----------------------------------------------------index  vacios -----------------------------------------------
@auth_bp.route('/bovinos')
def bovinos():
    return render_template('bovinos/index.html')


@auth_bp.route('/salida')
def salida():
    
    return render_template('inicio/index3.html')

@auth_bp.route('/salida1')
def salida1():
    
    return render_template('inicio/index.html')

@auth_bp.route('/operarios')
def operarios():
    data = Animales.query.all()
    return render_template('animal/index.html', data=data)  # Asegúrate de que este archivo existe

@auth_bp.route('/controles')
def controles():
    return render_template('control/index.html') # Asegúrate de que este archivo existe

@auth_bp.route('/praderas')
def praderas():
    return render_template('pradera/index.html')  # Asegúrate de que este archivo existe




