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
    title = db.Column(db.String(2), nullable=False)
    afNum = db.Column(db.String(5))
    #TODO Remove title + afNum and add 'Name'

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
        return "User('{self.email}')"				# Detta är det man får tillbaks om man printar objektet. Alltså inte PW eller id, bara mailen

# Kundinformation samt alla svar som vi kommer att hämta ner från Surveymonkey kommer att sparas i objekt och skapas i classen Responses nedan
class Responses(db.Model, UserMixin):
    # Initial setup questions
    response_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(20))
    # Gathered by the interviewer
    afNum = db.Column(db.String(150))
    creator = db.Column(db.String(150))
    custOrgNum = db.Column(db.String(150), unique=True)
    custCompName = db.Column(db.String(150))
    custNumCars = db.Column(db.String(150))
    custCompContact = db.Column(db.String(150))
    custCompEmail = db.Column(db.String(150))
    custCompPhone = db.Column(db.String(150))
    q9 = db.Column(db.String(500))
    q10 = db.Column(db.String(500))
    q11 = db.Column(db.String(500))
    q12 = db.Column(db.String(500))
    q13 = db.Column(db.String(500))
    q14 = db.Column(db.String(500))
    q15 = db.Column(db.String(500))
    q16 = db.Column(db.String(500))
    q17 = db.Column(db.String(500))
    q18 = db.Column(db.String(500))
    q19 = db.Column(db.String(500))
    q20 = db.Column(db.String(500))
    q21 = db.Column(db.String(500))
    q22 = db.Column(db.String(500))
    q23 = db.Column(db.String(500))
    q24 = db.Column(db.String(500))
    q25 = db.Column(db.String(500))
    q26 = db.Column(db.String(500))
    q27 = db.Column(db.String(500))
    q28 = db.Column(db.String(500))
    q29 = db.Column(db.String(500))
    q30 = db.Column(db.String(500))
    q31 = db.Column(db.String(500))
    q32 = db.Column(db.String(500))
    q33 = db.Column(db.String(500))
    q34 = db.Column(db.String(500))
    q35 = db.Column(db.String(500))
    q36 = db.Column(db.String(500))
    q37 = db.Column(db.String(500))
    q38 = db.Column(db.String(500))
    q39 = db.Column(db.String(500))
    q40 = db.Column(db.String(500))
    q41 = db.Column(db.String(500))
    q42 = db.Column(db.String(500))
    q43 = db.Column(db.String(500))
    q44 = db.Column(db.String(500))
    q45 = db.Column(db.String(500))
    q46 = db.Column(db.String(500))
    q47 = db.Column(db.String(500))
    q48 = db.Column(db.String(500))
    q49 = db.Column(db.String(500))
    q50 = db.Column(db.String(500))
    q51 = db.Column(db.String(500))
    q52 = db.Column(db.String(500))
    q53 = db.Column(db.String(500))
    q54 = db.Column(db.String(500))
    q55 = db.Column(db.String(500))
    q56 = db.Column(db.String(500))
    q57 = db.Column(db.String(500))
    q58 = db.Column(db.String(500))
    q59 = db.Column(db.String(500))
    q60 = db.Column(db.String(500))
    q61 = db.Column(db.String(500))
    q62 = db.Column(db.String(500))
    q63 = db.Column(db.String(500))
    q64 = db.Column(db.String(500))
    q65 = db.Column(db.String(500))
    q66 = db.Column(db.String(500))
    q67 = db.Column(db.String(500))
    q68 = db.Column(db.String(500))
    q69 = db.Column(db.String(500))
    q70 = db.Column(db.String(500))
    q71 = db.Column(db.String(500))
    q72 = db.Column(db.String(500))
    q73 = db.Column(db.String(500))
    q74 = db.Column(db.String(500))
    q75 = db.Column(db.String(500))
    q76 = db.Column(db.String(500))
    q77 = db.Column(db.String(500))
    q78 = db.Column(db.String(500))
    q79 = db.Column(db.String(500))
    q80 = db.Column(db.String(500))
    q81 = db.Column(db.String(500))
    q82 = db.Column(db.String(500))
    q83 = db.Column(db.String(500))
    q84 = db.Column(db.String(500))
    q85 = db.Column(db.String(500))
    q86 = db.Column(db.String(500))
    q87 = db.Column(db.String(500))
    q88 = db.Column(db.String(500))
    q89 = db.Column(db.String(500))
    q90 = db.Column(db.String(500))
    q91 = db.Column(db.String(500))
    q92 = db.Column(db.String(500))
    q93 = db.Column(db.String(500))
    q94 = db.Column(db.String(500))
    q95 = db.Column(db.String(500))
    q96 = db.Column(db.String(500))
    q97 = db.Column(db.String(500))
    q98 = db.Column(db.String(500))
    q99 = db.Column(db.String(500))
    q100 = db.Column(db.String(500))
    q101 = db.Column(db.String(500))
    q102 = db.Column(db.String(500))
    q103 = db.Column(db.String(500))
    q104 = db.Column(db.String(500))
    q105 = db.Column(db.String(500))
    q106 = db.Column(db.String(500))
    q107 = db.Column(db.String(500))
    q108 = db.Column(db.String(500))
    q109 = db.Column(db.String(500))
    q110 = db.Column(db.String(500))
    q111 = db.Column(db.String(500))
    q112 = db.Column(db.String(500))
    q113 = db.Column(db.String(500))
    q114 = db.Column(db.String(500))
    q115 = db.Column(db.String(500))
    q116 = db.Column(db.String(500))
    q117 = db.Column(db.String(500))
    q118 = db.Column(db.String(500))
    q119 = db.Column(db.String(500))
    q120 = db.Column(db.String(500))
    q121 = db.Column(db.String(500))
    q122 = db.Column(db.String(500))
    q123 = db.Column(db.String(500))
    q124 = db.Column(db.String(500))
    q125 = db.Column(db.String(500))
    q126 = db.Column(db.String(500))
    q127 = db.Column(db.String(500))
    q128 = db.Column(db.String(500))
    q129 = db.Column(db.String(500))
    q130 = db.Column(db.String(500))
    q131 = db.Column(db.String(500))
    q132 = db.Column(db.String(500))
    q133 = db.Column(db.String(500))
    q134 = db.Column(db.String(500))
    q135 = db.Column(db.String(500))
    q136 = db.Column(db.String(500))
    q137 = db.Column(db.String(500))
    q138 = db.Column(db.String(500))
    q139 = db.Column(db.String(500))
    q140 = db.Column(db.String(500))
    q141 = db.Column(db.String(500))
    q142 = db.Column(db.String(500))
    q143 = db.Column(db.String(500))
    q144 = db.Column(db.String(500))
    q145 = db.Column(db.String(500))
    q146 = db.Column(db.String(500))
    q147 = db.Column(db.String(500))
    q148 = db.Column(db.String(500))
    q149 = db.Column(db.String(500))
    q150 = db.Column(db.String(500))
    q151 = db.Column(db.String(500))
    q152 = db.Column(db.String(500))
    q153 = db.Column(db.String(500))
    q154 = db.Column(db.String(500))
    q155 = db.Column(db.String(500))
    q156 = db.Column(db.String(500))
    q157 = db.Column(db.String(500))
    q158 = db.Column(db.String(500))
    q159 = db.Column(db.String(500))
    q160 = db.Column(db.String(500))
    q161 = db.Column(db.String(500))
    q162 = db.Column(db.String(500))
    q163 = db.Column(db.String(500))
    q164 = db.Column(db.String(500))
    q165 = db.Column(db.String(500))
    q166 = db.Column(db.String(500))
    q167 = db.Column(db.String(500))
    q168 = db.Column(db.String(500))
    q169 = db.Column(db.String(500))
    q170 = db.Column(db.String(500))
    q171 = db.Column(db.String(500))
    q172 = db.Column(db.String(500))

    # Den information som skrivs tillbaks om man printar objektet
    def __repr__(self):
        return f"Responses('{self.response_id}', '{self.afNum}', '{self.creator}', '{self.custCompName}', '{self.custCompContact}')"

    # Metod som returnerar alla svar, hårdkodat, i en lista så att man kan iterera igenom denna när man renderar HTML-dokumentet på enkelt sätt
    def return_responses(self):
        # TODO: Iterate through the stored responses and only return the questions with not null answers
        return [
            self.afNum,
            self.creator,
            self.custOrgNum,
            self.custCompName,
            self.custNumCars,
            self.custCompContact,
            self.custCompEmail,
            self.custCompPhone,
            self.q9,
            self.q10,
            self.q11,
            self.q12,
            self.q13,
            self.q14,
            self.q15,
            self.q16,
            self.q17,
            self.q18,
            self.q19,
            self.q20,
            self.q21,
            self.q22,
            self.q23,
            self.q24,
            self.q25,
            self.q26,
            self.q27,
            self.q28,
            self.q29,
            self.q30,
            self.q31,
            self.q32,
            self.q33,
            self.q34,
            self.q35,
            self.q36,
            self.q37,
            self.q38,
            self.q39,
            self.q40,
            self.q41,
            self.q42,
            self.q43,
            self.q44,
            self.q45,
            self.q46,
            self.q47,
            self.q48,
            self.q49,
            self.q50,
            self.q51,
            self.q52,
            self.q53,
            self.q54,
            self.q55,
            self.q56,
            self.q57,
            self.q58,
            self.q59,
            self.q60,
            self.q61,
            self.q62,
            self.q63,
            self.q64,
            self.q65,
            self.q66,
            self.q67,
            self.q68,
            self.q69,
            self.q70,
            self.q71,
            self.q72,
            self.q73,
            self.q74,
            self.q75,
            self.q76,
            self.q77,
            self.q78,
            self.q79,
            self.q80,
            self.q81,
            self.q82,
            self.q83,
            self.q84,
            self.q85,
            self.q86,
            self.q87,
            self.q88,
            self.q89,
            self.q90,
            self.q91,
            self.q92,
            self.q93,
            self.q94,
            self.q95,
            self.q96,
            self.q97,
            self.q98,
            self.q99,
            self.q100,
            self.q101,
            self.q102,
            self.q103,
            self.q104,
            self.q105,
            self.q106,
            self.q107,
            self.q108,
            self.q109,
            self.q110,
            self.q111,
            self.q112,
            self.q113,
            self.q114,
            self.q115,
            self.q116,
            self.q117,
            self.q118,
            self.q119,
            self.q120,
            self.q121,
            self.q122,
            self.q123,
            self.q124,
            self.q125,
            self.q126,
            self.q127,
            self.q128,
            self.q129,
            self.q130,
            self.q131,
            self.q132,
            self.q133,
            self.q134,
            self.q135,
            self.q136,
            self.q137,
            self.q138,
            self.q139,
            self.q140,
            self.q141,
            self.q142,
            self.q143,
            self.q144,
            self.q145,
            self.q146,
            self.q147,
            self.q148,
            self.q149,
            self.q150,
            self.q151,
            self.q152,
            self.q153,
            self.q154,
            self.q155,
            self.q156,
            self.q157,
            self.q158,
            self.q159,
            self.q160,
            self.q161,
            self.q162,
            self.q163,
            self.q164,
            self.q165,
            self.q166,
            self.q167,
            self.q168,
            self.q169,
            self.q170,
            self.q171,
            self.q172
        ]
