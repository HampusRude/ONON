import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

#os.environ['DB_URI'] = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user='HampusRude@hampustest',pw='Password!',url='hampustest.postgres.database.azure.com',db='postgres')
os.environ['DB_URI'] = 'sqlite:///site.db'
os.environ['SECRET_KEY'] = 'c67a60abf8486349a4d5ad912aaf0d1f'
os.environ['SM_ACCESS_TOKEN'] = 'eu8UCOb1ARZae00whmCKNwA0d-kYUfA45emNHAvblRVbZUD7fS8NgITq.Bo34b88zKEz97YERLKNj.T0Y3HiRFhqr5jXnhjIi3J1POlFNJ7ZR03B8JmkAv-jkGvUfjf9'
os.environ['MAIL_SERVER'] = 'smtp.googlemail.com'
os.environ['MAIL_PORT'] = '587'
os.environ['MAIL_USERNAME'] = 'noreplybehovsanalystest@gmail.com'
os.environ['MAIL_PASSWORD'] = 'SecretPassword!'


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = os.environ['MAIL_SERVER']
app.config['MAIL_PORT'] = os.environ['MAIL_PORT']
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
mail = Mail(app)

from app import routes