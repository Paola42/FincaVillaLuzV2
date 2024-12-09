# config.py
import secrets

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///finca_villaluz.db'
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1:3306/fincaVillaLuzsena'
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:2hefbFfDEc-HFd1fhc2DhBCCgh-HCB65@monorail.proxy.rlwy.net:20020/Libreria1'
    #SQLALCHEMY_DATABASE_URI = 'mysql+mysqlclient://root:2hefbFfDEc-HFd1fhc2DhBCCgh-HCB65@monorail.proxy.rlwy.net:20020/Libreria1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secrets.token_hex(16)
    WTF_CSRF_ENABLED = True  # Activar CSRF
    
    # Configuración de correo
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587  # Usa el puerto 587 para TLS
MAIL_USE_TLS = True # Habilita TLS
MAIL_USERNAME = 'juanespitia538@gmail.com'
MAIL_PASSWORD = 'ezad nxka btiy gjsx'  # Esta debe ser tu contraseña de aplicación
MAIL_DEFAULT_SENDER = 'juanespitia538@gmail.com'  # Corrige el typo aquí
    