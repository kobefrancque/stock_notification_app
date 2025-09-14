from flask_sqlalchemy import SQLAlchemy
import os 

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    sp500_alert = db.Column(db.Boolean, nullable=False)