from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

#
# Varje sida man kommer in på (förutom just förstasidan) har någon form av "Form"
# Form = det som vi fyller mittenpartiet med i våra HTML-dokument 
# RegistrationForm innehåller exempelvis i sin ruta: 
# 		- Stringfield för email
#		- PasswordField för password
#		- PasswordField för confirm password
# 		- SubmitField som är knappen man klickar på när man har fyllt i alla fields
#

# Form för registrering av användarkonto på hemsidan
class RegistrationForm(FlaskForm):
	# Input fields and requirements
	email = StringField('E-mail', validators=[DataRequired(), Email()])
	password = PasswordField('Lösenord', validators=[DataRequired()])
	confirm_password = PasswordField('Bekräfta lösenord',
		validators=[DataRequired(), EqualTo('password')])
	company = SelectField('Företag', choices=[('VF', 'Välj företag'),('V', 'Volvo'), ('VW', 'Volkswagen'), ('A', 'Audi'), ('S', 'Skoda')], validators=[DataRequired()]) # Vilket företag jobbar personen i fråga på
	submit = SubmitField('Registrera')

	# Metod som används för att kolla att det inte redan finns en email i databasen som användare skriver i
	# Metodanropet görs när den används i routes
	def validate_email(self, email):
		email = User.query.filter_by(email=email.data).first()
		if email:
			raise ValidationError('Mailadressen finns redan. Glömt Lösenordet? Annars välj en annan.')


# Form för att logga in, påminner lite om RegistrationForm
# Input checkas mot databasen först när man använder sig av Formen i routes.py
class LoginForm(FlaskForm):
	# Input fields and requirements
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Lösenord', validators=[DataRequired()])
	remember = BooleanField('Kom igåg mig')
	submit = SubmitField('Logga in')


# Form för att uppdatera kontoinformation
class UpdateAccountForm(FlaskForm):
	# Input fields and requirements
	#email = StringField('Email', validators=[DataRequired(), Email()])
	old_password = PasswordField('Nuvarande lösenord', validators=[DataRequired()])
	new_password = PasswordField('Nytt lösenord', validators=[DataRequired()])
	confirm_password = PasswordField('Konfirmera nytt lösenord', validators=[DataRequired(), EqualTo('new_password')])
	submit = SubmitField('Uppdatera lösenord')

	'''
	def validate_email(self, email):
		if email.data != current_user.email:
			email = User.query.filter_by(email=email.data).first()
			if email:
				raise ValidationError('Mailadressen finns redan. Välj en annan.')
	'''
class RequestResetForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	submit = SubmitField('Skicka lösonordsåterställning')

	# Kollar ifall emailen finns
	def validate_email(self, email):
		email = User.query.filter_by(email=email.data).first()
		if email is None:
			raise ValidationError('Det finns inget konto med den emailen. Du måste registrera dig först')

# Input-form och knapp som finns när man återställer lösenord
class ResetPasswordForm(FlaskForm):
	password = PasswordField('lösenord', validators=[DataRequired()])
	confirm_password = PasswordField('Bekräfta lösenord', 
		validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Återställ lösenord')

# Ingenting som används i dagsläget
class ChangeResponseForm(FlaskForm):
	updated_response = StringField('Nytt svar', validators=[DataRequired()])
	submit = SubmitField('Uppdatera svar')