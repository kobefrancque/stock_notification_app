from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from forms import RegistrationForm
from database import db, Users

load_dotenv()

app = Flask(__name__, template_folder='templates')
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'database.db')}"
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    registration_form = RegistrationForm()
    if request.method == 'GET':
        return render_template('registration.html', registration_form=registration_form)
    elif request.method == 'POST':
        if registration_form.validate_on_submit():
            username = registration_form.username.data
            password = registration_form.password.data
            phone = registration_form.phone.data
            sp500_enabled = registration_form.sp500_enabled.data

            new_user = Users(
                username=username,
                password=password,
                phone_number=phone,
                sp500_alert=sp500_enabled
            )

            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('index'))
        else:
            return render_template('registration.html', registration_form=registration_form)  # Form validation failed - return form with errors

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(host='0.0.0.0', debug=True)
