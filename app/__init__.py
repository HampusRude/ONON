from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c67a60abf8486349a4d5ad912aaf0d1f'

#params = urllib.parse.quote_plus("DRIVER={ODBC Driver 13 for SQL Server};SERVER=onondb.database.windows.net;DATABASE=onondb;UID=rudahl@onondb;PWD=t2jguGe83oxwYgeV")
#db_uri = "mssql+pyodbc:///?odbc_connect=%s" % params
# db_uri = 'mssql+pyodbc://rudahl:t2jguGe83oxwYgeV@ononapp.database.windows.net:1433/onondb?driver=ODBC+Driver+13+for+SQL+Server'

# db_uri = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user='HampusRude@hampustest',pw='Password!',url='hampustest.postgres.database.azure.com',db='postgres')
db_uri = 'sqlite:///site.db'

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

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