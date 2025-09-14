from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8, max=20)])
    phone = StringField('phone', validators=[DataRequired(), Regexp(r'^\d{10}$', message="Phone number must be 10 digits.")])
    sp500_enabled = BooleanField('SP500 alerts', default=False)
    submit = SubmitField('register')

class LoginForm(FlaskForm):
    pass