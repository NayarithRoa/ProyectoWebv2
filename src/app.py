import json
from flask import Flask, render_template, request, redirect, url_for, flash
from flaskext.mysql import MySQL   
from decouple import config 
from flask_mail import *
from random import *
from itsdangerous import URLSafeTimedSerializer
#from flask_wtf.csrf import CSRFProtect
from config import config
from flask_login import LoginManager, login_user, logout_user, login_required

# Modelos:
from models.ModelUser import ModelUser

# Entidades:
from models.entidades.Usuario import UserLogin, UserRegister
app = Flask(__name__)

#csrf = CSRFProtect()
db = MySQL(app)
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_DB']='seguimientousuarios'
db.init_app(app)#Crear la conexion con los datos anteriores asignados
login_manager_app = LoginManager(app)


#DATOS PARA EL ENVIO CORREO DE CONFIRMACIÓN
with open('src/config.json', 'r') as f:
    params=json.load(f)['param']

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']=params['gmail-user']
app.config['MAIL_PASSWORD']=params['gmail-password']
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
app.config['SECRET_KEY']="secret"
mail=Mail(app)
#enviar algunos datos a entornos que no son de confianza y luego recuperarlos más tarde.
s=URLSafeTimedSerializer(app.config["SECRET_KEY"])

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/')
def index():
    return render_template('auth/registro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = UserLogin(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                logged_user = ModelUser.login(db, user)
                return redirect(url_for('home'))
            else:
                flash("Clave invalida...")
                return render_template('auth/login.html')
        else:
            flash("Usuario no encontrado...")
            return render_template('auth/login.html')
        
    else:
        return render_template('auth/login.html')

@app.route('/registroDatosBasicos', methods=['POST'])
def registroDatosBasicos():
    if request.method == 'POST':
        _sexo=request.form['sexo']
        _edad=request.form['edad']
        _estadocivil=request.form['estadocivil']
        _estrato=request.form['estrato']
        _vivienda=request.form['vivienda']
        _escolaridad=request.form['escolaridad']
        _ocupacion=request.form['ocupacion']
        _sistemaSalud=request.form['sistemaSalud']
        _diagnosticomedico=request.form['diagnosticomedico']
        _discapacidad=request.form['discapacidad']

        if _estrato=='' or _vivienda=='':
            flash("Datos incompletos")   
            return render_template('datosBasicosParte2.html')
            
        else:
            nombre='naya1'
            telefono='3023925456'
            clave='1234567'
            cuidador=1
            user = UserRegister(0,nombre,telefono, clave,_sexo, _edad,_estrato, _vivienda, _escolaridad,_ocupacion,_sistemaSalud,_discapacidad,_diagnosticomedico,cuidador, _estadocivil)
            logged_user = ModelUser.registrardatosbasicos(db, user)
            flash("Datos actualizados") 
            return redirect(url_for('login'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/registro')
def registro():
    return render_template('auth/registro.html')

#Envía correo de confirmacion cuando esta creando un nuevo usuario en la app
@app.route("/verificarlinkemail", methods=['GET', 'POST'])
def verificarlinkemail():
    gmail=request.form['email']
    name=request.form['name']
    phone=request.form['phone']
    clave=request.form['clave']
    user = UserLogin(0,name,gmail,phone, clave)
    logged_user = ModelUser.registrarusuario(db, user)
    #flash("Usuario registrado") 

    token= s.dumps(gmail, salt='email-confirmation-key')
    msg=Message('Confirmación registro', sender=params['gmail-user'],recipients=[gmail])
    link=url_for('confirmemail', token=token, _external=True)
    msg.body="Hola, \n Gracias por registrarte en nuestra aplicacion. \n Tu codigo de verificacion es: " + link
    mail.send(msg)
    return "<h2>Verifique su correo para confirmar el registro. </h2>"

@app.route('/confirmemail/<token>')
def confirmemail(token):
    try:
        email=s.loads(token,salt='email-confirmation-key', max_age=60)
    except Exception:
        return "<h1> Link expiró </h1>"
    return "<h1> Confirmacion hecha. </h1>"


@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"
    
def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    #csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()