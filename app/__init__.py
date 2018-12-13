from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c67a60abf8486349a4d5ad912aaf0d1f'

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user='HampusRude@hampustest',pw='Password!',url='hampustest.postgres.database.azure.com',db='postgres')

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/onontest'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'noreplybehovsanalystest@gmail.com'
app.config['MAIL_PASSWORD'] = 'testing123!'
mail = Mail(app)

from app import routes