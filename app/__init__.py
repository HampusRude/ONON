from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c67a60abf8486349a4d5ad912aaf0d1f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Ehzfxnj5!@localhost/ononAB'

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

'''
# Configuring webhook
access_token = "eu8UCOb1ARZae00whmCKNwA0d-kYUfA45emNHAvblRVbZUD7fS8NgITq.Bo34b88zKEz97YERLKNj.T0Y3HiRFhqr5jXnhjIi3J1POlFNJ7ZR03B8JmkAv-jkGvUfjf9"
s = requests.session()
s.headers.update({
  "Authorization": "Bearer %s" % access_token,
  "Content-Type": "application/json"
})

payload = {
  "name": "My Webhook",
  "event_type": "response_completed",
  "object_type": "survey",
  "object_ids": ["160620263"],
  "subscription_url": "http://727ee712.ngrok.io/webhook"
}
url = "https://api.surveymonkey.com/v3/webhook"
s.post(url, json=payload)
'''
from app import routes