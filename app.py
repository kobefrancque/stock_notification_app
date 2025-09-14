from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, template_folder='templates')
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'database.db')}"

db = SQLAlchemy(app)

class Users():
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    sp500_alert = db.Column(db.Boolean, nullable=False)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(host='0.0.0.0', debug=True)
