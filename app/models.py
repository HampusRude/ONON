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
	__abstract__ = True
	id = db.Column(db.Integer, primary_key=True)	# Unikt för varje användare, används när man skapar unika "reset-password-tokens"
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	title = db.Column(db.String(2), nullable=False)
	afnum = db.Column(db.String(5))

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
	__abstract__ = True
	response_id = db.Column(db.Integer, primary_key = True)
	timestamp = db.Column(db.String(150))
	date = db.Column(db.String(150))
	afNum = db.Column(db.String(150))
	creator = db.Column(db.String(150))
	custOrgNum = db.Column(db.String(150))
	custCompName = db.Column(db.String(150))
	custCompContact = db.Column(db.String(150))
	custCompEmail = db.Column(db.String(150))
	custCompPhone = db.Column(db.String(150))
	q1 = db.Column(db.String(150))
	q2 = db.Column(db.String(150))
	q3 = db.Column(db.String(150))
	q4 = db.Column(db.String(150))
	q5 = db.Column(db.String(150))
	q6 = db.Column(db.String(150))
	q7 = db.Column(db.String(150))
	q8 = db.Column(db.String(150))
	q9 = db.Column(db.String(150))
	q10 = db.Column(db.String(150))
	q11 = db.Column(db.String(150))
	q11_1 = db.Column(db.String(150))
	q12 = db.Column(db.String(150))
	q13 = db.Column(db.String(150))
	q14 = db.Column(db.String(150))
	q15 = db.Column(db.String(150))
	q16 = db.Column(db.String(150))
	q17 = db.Column(db.String(150))
	q18 = db.Column(db.String(150))
	q19 = db.Column(db.String(150))
	q20 = db.Column(db.String(150))
	q21 = db.Column(db.String(150))
	q22 = db.Column(db.String(150))
	q23 = db.Column(db.String(150))
	q24 = db.Column(db.String(150))
	q25 = db.Column(db.String(150))
	q26 = db.Column(db.String(150))
	q27 = db.Column(db.String(150))
	q28 = db.Column(db.String(150))
	q29 = db.Column(db.String(150))
	q30 = db.Column(db.String(150))
	q31 = db.Column(db.String(150))
	q32 = db.Column(db.String(150))
	q33 = db.Column(db.String(150))
	q34 = db.Column(db.String(150))
	q35 = db.Column(db.String(150))
	q36 = db.Column(db.String(150))
	q37 = db.Column(db.String(150))
	q38 = db.Column(db.String(150))
	q39 = db.Column(db.String(150))
	q40 = db.Column(db.String(150))
	q41 = db.Column(db.String(150))
	q42 = db.Column(db.String(150))
	q43 = db.Column(db.String(150))
	q44 = db.Column(db.String(150))
	q45 = db.Column(db.String(150))
	q46 = db.Column(db.String(150))
	q47 = db.Column(db.String(150))
	q48 = db.Column(db.String(150))
	q49 = db.Column(db.String(150))
	q50 = db.Column(db.String(150))
	q51 = db.Column(db.String(150))
	q52 = db.Column(db.String(150))
	q53 = db.Column(db.String(150))
	q54 = db.Column(db.String(150))
	q55 = db.Column(db.String(150))
	q56 = db.Column(db.String(150))
	q57 = db.Column(db.String(150))
	q58 = db.Column(db.String(150))
	q59 = db.Column(db.String(150))
	q60 = db.Column(db.String(150))
	q61 = db.Column(db.String(150))
	q62 = db.Column(db.String(150))
	q63 = db.Column(db.String(150))
	q64 = db.Column(db.String(150))
	q65 = db.Column(db.String(150))
	q66 = db.Column(db.String(150))
	q67 = db.Column(db.String(150))
	q68 = db.Column(db.String(150))
	q69 = db.Column(db.String(150))
	q70 = db.Column(db.String(150))
	q71 = db.Column(db.String(150))
	q72 = db.Column(db.String(150))
	q73 = db.Column(db.String(150))
	q74 = db.Column(db.String(150))
	q75 = db.Column(db.String(150))
	q76 = db.Column(db.String(150))
	q77 = db.Column(db.String(150))
	q78 = db.Column(db.String(150))
	q79 = db.Column(db.String(150))
	q80 = db.Column(db.String(150))
	q81 = db.Column(db.String(150))
	q82 = db.Column(db.String(150))
	q83 = db.Column(db.String(150))
	q84 = db.Column(db.String(150))
	q85 = db.Column(db.String(150))
	q86 = db.Column(db.String(150))
	q87 = db.Column(db.String(150))
	q88 = db.Column(db.String(150))
	q89 = db.Column(db.String(150))
	q90 = db.Column(db.String(150))
	q91 = db.Column(db.String(150))
	q92 = db.Column(db.String(150))
	q93 = db.Column(db.String(150))
	q94 = db.Column(db.String(150))
	q95 = db.Column(db.String(150))
	q96 = db.Column(db.String(150))
	q97 = db.Column(db.String(150))
	q98 = db.Column(db.String(150))
	q99 = db.Column(db.String(150))
	q100 = db.Column(db.String(150))
	q101 = db.Column(db.String(150))
	q102 = db.Column(db.String(150))
	q103 = db.Column(db.String(150))
	q104 = db.Column(db.String(150))
	q105 = db.Column(db.String(150))
	q106 = db.Column(db.String(150))
	q107 = db.Column(db.String(150))
	q108 = db.Column(db.String(150))
	q109 = db.Column(db.String(150))
	q110 = db.Column(db.String(150))
	q111 = db.Column(db.String(150))
	q112 = db.Column(db.String(150))
	q113 = db.Column(db.String(150))
	q114 = db.Column(db.String(150))
	q115 = db.Column(db.String(150))
	q116 = db.Column(db.String(150))
	q117 = db.Column(db.String(150))
	q118 = db.Column(db.String(150))
	q119 = db.Column(db.String(150))
	q120 = db.Column(db.String(150))
	q121 = db.Column(db.String(150))
	q122 = db.Column(db.String(150))
	q123 = db.Column(db.String(150))
	q124 = db.Column(db.String(150))
	q125 = db.Column(db.String(150))
	q126 = db.Column(db.String(150))
	q127 = db.Column(db.String(150))
	q128 = db.Column(db.String(150))


	# Den information som skrivs tillbaks om man printar objektet
	def __repr__(self):
		return f"Responses('{self.afNum}', '{self.custCompName}', '{self.custOrgNum}', '{self.date}')"

	# Metod som returnerar alla svar, hårdkodat, i en lista så att man kan iterera igenom denna när man renderar HTML-dokumentet på enkelt sätt
	def return_responses(self):
		# TODO: Iterate through the stored responses and only return the questions with not null answers
		return {
			'q1': self.q1,
			'q2': self.q2,
			'q3': self.q3,
			'q4': self.q4,
			'q5': self.q5,
			'q6': self.q6}