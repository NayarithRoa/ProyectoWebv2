import json
from flask import Flask, render_template, request, redirect, url_for, flash
from flaskext.mysql import MySQL
from flask_mail import *
from random import *
from itsdangerous import URLSafeTimedSerializer
#from flask_wtf.csrf import CSRFProtect
from config import config
from flask_login import LoginManager, login_user, logout_user, login_required

# Modelos:
from models.ModelUser import ModelUser

# Entidades:
from models.entidades.Usuario import User
app = Flask(__name__)

#csrf = CSRFProtect()
db = MySQL(app)
db.init_app(app)
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
    #return redirect(url_for('login'))
    return render_template('auth/registro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form['username'], request.form['password'])
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

@app.route("/verificarlinkemail", methods=['GET', 'POST'])
def verificarlinkemail():
    gmail=request.form['email']
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