from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

# Form för registrering av användarkonto på hemsidan
# Lösenord självgenererasi routes.py och skickas till det som skrivs in i email nedan
class RegistrationForm(FlaskForm):
	email = StringField('E-mail', validators=[DataRequired(), Email()])
	title = SelectField('Titel', choices=[('VT', 'Välj titel'), ('VG', 'Volkswagen chef'), ('AF', 'Återförsäljare')], validators=[DataRequired()]) # Vilken titel användare kommer att ha, WG kan se allt, ÅF kan bara se det som respektive ÅF har lagt in
	afNum = StringField('ÅF-nummer')
	submit = SubmitField('Registrera')

	# Kontrollera om email-adressen redan finns i databasen
	def validate_email(self, email):
		email = User.query.filter_by(email=email.data).first()
		if email:
			raise ValidationError('Mailadressen finns redan. Glömt Lösenordet? Annars välj en annan.')

# Form som används för att ta emot input när en användare loggar in
class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Lösenord', validators=[DataRequired()])
	remember = BooleanField('Kom ihåg mig')
	submit = SubmitField('Logga in')

# Form för att uppdatera kontoinformation
class UpdateAccountForm(FlaskForm):
	old_password = PasswordField('Nuvarande lösenord', validators=[DataRequired()])
	new_password = PasswordField('Nytt lösenord', validators=[DataRequired()])
	confirm_password = PasswordField('Konfirmera nytt lösenord', validators=[DataRequired(), EqualTo('new_password')])
	submit = SubmitField('Uppdatera lösenord')

class DeleteAccountForm(FlaskForm):
	password = PasswordField('Lösenord')
	confirm_password = PasswordField('Konfirmera nytt lösenord', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Radera konto')

# Form som används i reset password request
class RequestResetForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	submit = SubmitField('Skicka lösonordsåterställning')

	# Kontrollera om email-adressen redan finns i databasen
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

# Form som används för att uppdatera ett svar
class UpdateResponseForm(FlaskForm):
	updated_response = TextAreaField('Nytt svar', validators=[DataRequired()])
	submit = SubmitField('Uppdatera svar')