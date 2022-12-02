from flask import *
from flask_mail import *
from random import *

app = Flask(__name__)

with open('config.json', 'r') as f:
    params=json.load(f)['param']
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']=params['gmail-user']
app.config['MAIL_USERNAME']=params['gmail-password']
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)

@app.route('')
def index():
    return render_template('auth/registro.html')
