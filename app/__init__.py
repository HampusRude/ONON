import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


db_uri = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=os.environ['APPSETTING_DB_USER'],
                                                               pw=os.environ['APPSETTING_DB_PWD'],
                                                               url=os.environ['APPSETTING_DB_URL'],
                                                               db=os.environ['APPSETTING_DB_DB'])

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['APPSETTING_SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['APPSETTING_DB_URI']

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = os.environ['APPSETTING_MAIL_SERVER']
app.config['MAIL_PORT'] = os.environ['APPSETTING_MAIL_PORT']
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ['APPSETTING_MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['APPSETTING_MAIL_PASSWORD']
mail = Mail(app)

from app import routes