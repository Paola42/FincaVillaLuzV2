# config.py
import secrets

class Config:
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///finca_villaluz.db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1:3306/fincaVillaLuzsena'
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:2hefbFfDEc-HFd1fhc2DhBCCgh-HCB65@monorail.proxy.rlwy.net:20020/Libreria1'
    #SQLALCHEMY_DATABASE_URI = 'mysql+mysqlclient://root:2hefbFfDEc-HFd1fhc2DhBCCgh-HCB65@monorail.proxy.rlwy.net:20020/Libreria1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secrets.token_hex(16)
    WTF_CSRF_ENABLED = True  # Activar CSRF
    
    # Configuración de correo
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'juanespitia538@gmail.com'
    MAIL_PASSWORD = 'nyig ysxt rlid shth'  # Esta debe ser tu contraseña de aplicación
    MAIL_DEFAULT_SENDER = 'juanespitia538@gmail.com'  # Corrige el typo aquí
