from flask import render_template, url_for, flash, redirect, request
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm, \
    UpdateResponseForm, DeleteAccountForm, DeleteResponseForn
from app import app, bcrypt, db, mail
from app.models import User, Responses
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
from app.q_dict import question_dict
from app.retrive_data import retrieve_data, add_response
import random, string, json


#
#	Detta är route-filen som exekverar olika saker beroende på klientens GET-request
#	T.ex. www.behovsanalys.se/kund kommer att rendera kund.html
#

# Renderar bara startsidan
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')


# Sitan med kundlistan skall öppnas
@app.route("/kund")
@login_required
def kund():
    responses = Responses.query.all()
    return render_template('kund3.html', responses=responses, title="Arkiv")


# Denna sida visar alla svar som en kund har gett
@app.route("/kund/<response_id>", methods = ['GET', 'POST'])
@login_required
def responses(response_id):
    # Hämtar response kopplat till företaget man klickat på
    form = DeleteResponseForn()
    responses = Responses.query.filter_by(response_id=response_id).first()
    if form.validate_on_submit():
        flash(f"Behovsanalys för kund {responses.q4} är nu raderad", "info")
        db.session.delete(responses)
        db.session.commit()
        return redirect(url_for('kund'))
    # Renderar responses.html, res = dict med svar, Questions = hårkodad dict med respektive fråga, form=Responseform som är skapad i Forms.py
    return render_template('responses.html', form=form, title=responses.q4, responses=responses, questions=question_dict, length=len(
        question_dict))

@app.route("/kund/<response_id>/<res>", methods=['GET', 'POST'])
@login_required
def updateResponse(response_id, res):
    form = UpdateResponseForm()
    responseForm = Responses.query.filter_by(response_id=response_id).first()
    response = getattr(responseForm, res)
    if form.validate_on_submit():
        setattr(responseForm, res, form.updated_response.data)  # Ändrar innehåll i objectet
        db.session.commit()  # Commitar ändringen till databasen
        flash(f'Svar för fråga: {question_dict[res]} uppdaterades', 'success')
        return redirect(url_for('responses', response_id=responseForm.response_id))
    elif request.method == 'GET':  # Om det är en GET request, dvs när man bara laddar sidan och inte stoppar in någonting i databasen
        form.updated_response.data = response  # Då lägger vi in det som finns i response i textfältet
    return render_template('updateresponse.html', response=response, form=form, question=question_dict[res])

# Denna sida är för att kunna skapa ett konto på servern
@app.route("/register", methods=['GET', 'POST'])  # Kan hantera både GET och POST requests. POST requests sker när man skickar in inloggningsdetaljer
def register():
    if current_user.admin != True:
        flash('Du måste ha adminkonto för att kunna registrera användare', 'danger')
        return redirect(url_for('home'))
    form = RegistrationForm()  # Om inte, hämta RegistrationForm från Forms.py, och sedan se Return statement nedan
    if form.validate_on_submit():  # OM SubmitField klickas, kör nedan
        first_password = randomString()  # Generera ett första lösenord
        print(first_password)
        # form.password.data = det som användaren har skrivit in i PasswordField (se forms.py). Detta hashas med flasks modul bcrypt
        hashed_password = bcrypt.generate_password_hash(first_password).decode('utf-8')
        user = User(email=form.email.data.lower(), password = hashed_password, admin=form.admin.data)# Inloggningsdetaljer sparas i ett objekt via clasen User från models.py som sparar parametrarna (ID, email, PW)
        send_register_email(user, first_password)   # Skickar inloggningsuppgifter till kontot
        db.session.add(user)  # SQLAlchemy kommando för att adda objektet
        db.session.commit()  # commitar till databasen
        flash(f'Konto skapat för {form.email.data}! Inloggningsinformation har skickats till kontoinnehavaren',
              'success')  # Givet att allt ovan fungerar så kommer en grön ('success') banner upp i toppen av sidan och konfirmerar att det gick
        #send_register_email(user, first_password)
        return redirect(url_for(
            'login'))  # För att samtidigt redirecta dig till login-sidan (url_for är en modul importerad från flask)
    return render_template('register.html', title='Register',
                           form=form)  # Om ingen är inloggad så renderas register.html tillsammans med RegistrationForm som hanterar registreringstrafiken

#TODO: Lägg till en felhanterare ifall mailen inte skulle fungera
def send_register_email(user, first_password):
    msg = Message('Ditt konto till www.vgsbehovsanalys.se',  # Mail-funktion från flask_mail
                  sender='noreply@on-on.se',
                  recipients=[
                      user.email])  # Mottagaren av mailet ska vara den mail som är angiven och finns i databasen
    # Nedanstående är själva mailet som mottagaren kommer att få från ONONABtest@gmail.com som det ser ut nu
    msg.body = f'''Nedan är dina inloggningsdetaljer till www.vgsbehovsanalys.se:
    
Emailadress: {user.email}
Lösenord: {first_password}

Klicka på länken nedan för att logga in och byta lösenord:
{url_for('account', _external=True)}
'''
    mail.send(
        msg)  # Skickar meddelandet, se __init__.py för att förstå hur konfigurationerna för detta fungerar, och GOOGLA


def randomString():
    length = 6
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


@app.route("/login", methods=['GET',
                              'POST'])  # Kan hantera både GET och POST requests. POST requests sker när man skickar in inloggningsdetaljer
def login():
    if current_user.is_authenticated:  # current_user är en modul importerad från flask_login som känner av om någon redan är inloggad
        return redirect(url_for('home'))  # Om så är fallet, rendera home.html
    form = LoginForm()  # Om inte, hämta RegistrationForm från Forms.py, och sedan se Return statement nedan
    if form.validate_on_submit():  # OM SubmitField klickas, kör nedan
        # Kod som kontrollerar om användaren finns i databasen
        user = User.query.filter_by(
            email=form.email.data).first()  # Försöker hämta användaren i databasen genom att kolla om det finns ett User-objekt med angiven email
        if user and bcrypt.check_password_hash(user.password,
                                               form.password.data):  # Om användarnamnet stämmer samt om lösenordet som användaren skrivit in i formen stämmer med det hashade lösenordet i databasen, kör nedan
            login_user(user,
                       remember=form.remember.data)  # login_user är en importerad modul från flask. remember är en form som finns i Forms.py. En check-box "remember me"
            next_page = request.args.get(
                'next')  # Funktion som tar dig till den sidan du va på innan, om du försökt klicka på kundsida men inte kommit åt den pga att du inte var inloggad, så ska du redirectas till den och inte första-sidan när du lyckats logga in
            flash('Välkommen, du är nu inloggad som ' + user.email, 'success')  # Grön banner som säger att det gick bra
            return redirect(next_page) if next_page else redirect(
                url_for('home'))  # Redirect till första-sidan om du inte försökt komma in på någonting annat innan
        else:
            flash('Email eller lösenord är felaktigt, försök igen', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', title='Login', form=form)  # Renderar login.html och skickar in formen


# Denna route renderar ingenting specielt, utan den kör flask-kommantod logout_user() och redirectar dig till första-sidan
@app.route("/logout")
def logout():
    flash(f"Du är nu utloggad från konto {current_user.email}. Välkommen åter ", "info")
    logout_user()
    return redirect(url_for('home'))


# Sida för att kunna ändra dina inloggningsuppgifter
@app.route("/account", methods=['GET', 'POST'])
@login_required  # Går bara att accessa om du är inloggad
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if bcrypt.check_password_hash(current_user.password, form.old_password.data):
            new_hashed_password = bcrypt.generate_password_hash(form.new_password.data).decode('utf-8')
            current_user.password = new_hashed_password
            db.session.commit()
            flash('Ditt lösenord har uppdaterats', 'success')
            return redirect(url_for('home'))
        else:
            flash('Fel lösenord angivet, försök igen', 'danger')
            return redirect(url_for('account'))
    return render_template('account.html', title='Konto', form=form)


@app.route("/account/delete", methods=['GET', 'POST'])
@login_required
def deleteAccount():
    form = DeleteAccountForm()
    if form.validate_on_submit():
        if bcrypt.check_password_hash(current_user.password, form.password.data):
            delete_this_user = User.query.filter_by(email=current_user.email).first()
            flash(f"Kontot för {current_user.email} är nu raderat", "danger")
            logout_user()
            db.session.delete(delete_this_user)
            db.session.commit()
            return redirect(url_for('home'))
        else:
            flash("Det angivna lösenordet var fel, var god försök igen", "danger")
            return redirect(url_for('deleteAccount'))
    return render_template('deleteaccount.html', title='Radera konto', form=form)



# Sida du kommer till när du klickat på "Glömt lösenord?"
@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()  # Form från forms.py
    if form.validate_on_submit():  # OM SubmitField klickas, kör nedan
        user = User.query.filter_by(
            email=form.email.data).first()  # Kollar i databasen om det finns en användare med angiven email, if so, hämta objektet
        send_reset_email(user)  # Anropa funktionen send_reset_email() (se nedan), och skicka med user-objektet
        flash('Ett mail har skickats med instruktioner för att återställa lösenordet',
              'info')  # Gul banner ('info') som säger att att återställningsmail har skickats till angiven email
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


def send_reset_email(user):
    token = user.get_reset_token()  # Skapar en unik "token" mha av User-objektet, googla detta för att få klarthet. Utan parameter så blir default livslängd 30min
    msg = Message('Password Reset Request',  # Mail-funktion från flask_mail
                  sender='noreply@ONONAB.com',
                  recipients=[
                      user.email])  # Mottagaren av mailet ska vara den mail som är angiven och finns i databasen
    # Nedanstående är själva mailet som mottagaren kommer att få från ONONABtest@gmail.com som det ser ut nu
    msg.body = f'''Klicka på följande länk för att återställa ditt lösenord:
{url_for('reset_token', token=token, _external=True)}
'''

    mail.send(
        msg)  # Skickar meddelandet, se __init__.py för att förstå hur konfigurationerna för detta fungerar, och GOOGLA


# Sida som du kommer till när du har klickat på länken som du får i mailet när du har glömt lösenordet
@app.route("/reset_password/<token>", methods=['GET',
                                               'POST'])  # Tokene'n som skapades mha User-objektet ovan kommer att läggas efter "/" i GET-requesten som kommer att användas för att validera att det är du (tidsbegränsad)
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)  # Metod som verifierar att det är rätt token samt plockar fram rätt objekt
    if user is None:  # Om det inte finns någon user eller om ditt token har "dött" (tar 30min), kör nedan
        flash('Felaktigt eller utgånget token', 'warning')  # Röd banner ('warning') med text om att det inte fungerar
        return redirect(url_for(
            'reset_request'))  # Skickar tillbaks en till sidan för att skapa ett nytt token och få ett nytt mail
    form = ResetPasswordForm()  # Form från forms.py
    if form.validate_on_submit():  # OM SubmitField klickas, kör nedan
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            'utf-8')  # Hashar det nya lösenordet som anges i PasswordField
        user.password = hashed_password  # Updaterar det aktuella user-objektet
        db.session.commit()  # commitar till databasen (viola det är nu ändrat)
        flash('Lösenordet är nu återstält! Du kan nu logga in igen', 'success')
        return redirect(url_for('login'))  # Redirectar dig till login så att du kan logga in med det nya lösenordet
    return render_template('reset_token.html', title='Reset Password', form=form)  # Renderar reset_token.html


# Kör retrieve_data som hämtar all data från survey monkey och lägger in i databasen.
# ---- Tillfällig lösning innan vi får webhooken och fungera ----
@app.route("/udb")
@login_required
def update_db():
    #retrieve_data()
    return render_template('home.html', title='Home')

# Webhook för att ta emote POST requests from Surveymonkey
@app.route("/webhook", methods=['POST', 'HEAD'])
def webhook():
    if request.method == 'HEAD':
        print("HEAD request")
        return ""
    elif request.method == 'POST':
        jsonData = json.loads(request.data)
        if (jsonData['event_type'] == 'response_completed'):
            response_id = jsonData['resources']['respondent_id']
            print("respondent ID: " + response_id)
            add_response(response_id)
        return "Post request successfully responded"