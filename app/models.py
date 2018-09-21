from app import db, login_manager, app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

#
# Information om användare sparas i objekt och skapas ur klassen User nedan
# User.id används inte till någonting i programmet förutom i bakgrunden av logon_manager samt när man skapar tokens
#

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)	# Unikt för varje användare, används när man skapar unika "reset-password-tokens"
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	company = db.Column(db.String(2), nullable=False) # Vilket företag som användaren arbetar på. Detta för att man bara ska kunna få upp sina unika kunder och inte andras

	# Metod för att skapa en token kopplat till en specifik användare om denne har glömt sitt lösenord. Detta gör när man är inne på /reset_password
	def get_reset_token(self, expires_sec=1800):
		s = Serializer(app.config['SECRET_KEY'], expires_sec)
		return s.dumps({'user_id': self.id}).decode('utf-8')	#Create the token with the user ID

	# Metod som används för att validera ett token av en klient
	# Statisk metod eftersom att vi inte skickar med self som en parameter
	@staticmethod
	def verify_reset_token(token):
		s = Serializer(app.config['SECRET_KEY'])	# Secret key används som "private key" av databasen. Det är en sträng som är definierad i __init__.py
		try:
			user_id = s.loads(token)['user_id']		# returnerar user_id för det aktuella tokenet
		except:
			return None
		return User.query.get(user_id)				# retuenerar User-objektet kopplat till användaren mha user_id

	def __repr__(self):
		return f"User('{self.email}')"				# Detta är det man får tillbaks om man printar objektet. Alltså inte PW eller id, bara mailen


# Kundinformation samt alla svar som vi kommer att hämta ner från Surveymonkey kommer att sparas i objekt och skapas i classen Responses nedan
class Responses(db.Model, UserMixin):
	representing = db.Column(db.String(2))		
	afnum = db.Column(db.Integer, primary_key=True)
	company = db.Column(db.String(30), unique=True)
	orgnum = db.Column(db.Integer, unique=True)
	kam = db.Column(db.String(30))
	email = db.Column(db.String(20))
	mobil = db.Column(db.Integer)
	q1 = db.Column(db.Integer)	#1-5
	q2 = db.Column(db.Integer)	#1-5
	q3 = db.Column(db.Integer)	#1-5
	q4 = db.Column(db.String(150))	#Öppen
	q5 = db.Column(db.String(150))	#Öppen
	q6 = db.Column(db.String(150))	#Öppen


	# Den information som skrivs tillbaks om man printar objektet
	def __repr__(self):
		return f"Responses('{self.afnum}', '{self.company}', '{self.orgnum}', '{self.kam}')"

	# Metod som returnerar alla svar, hårdkodat, i en lista så att man kan iterera igenom denna när man renderar HTML-dokumentet på enkelt sätt
	def return_responses(self):
		return [
			self.q1, 
			self.q2, 
			self.q3, 
			self.q4,
			self.q5,
			self.q6,]