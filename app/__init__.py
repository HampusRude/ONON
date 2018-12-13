from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c67a60abf8486349a4d5ad912aaf0d1f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://rudahl:t2jguGe83oxwYgeV@ononapp.database.windows.net:1433/onondb'

# Vad en annan använt för att synka upp SQLAlchemy mot Azure
# create_engine('mssql+pyodbc://{user_name}:{password}@{our_subdomain}.database.windows.net:1433/{our_database_name}', echo=True)


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ononabtest@gmail.com'
app.config['MAIL_PASSWORD'] = 'Qwe3945o!'
mail = Mail(app)

from app import routes