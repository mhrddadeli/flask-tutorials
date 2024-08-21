from flask import Flaskforms
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Lenght, Email, EQualTo


class RegistrationForm(Flaskforms):
    username = StringField(
        'username',
        validators=[
            DataRequired(),
            Length(min=6, max=20)
            ]
        )
    email = StringField(
        'email',
        validators=[
            DataRequired(),
            Email()
            ]
        ) 
    password = PasswordField(
        'password',
        validators=[
            DataRequired()
            ]
    )
    confirm_password = PasswordField(
        'confirm password',
        validators=[
            DataRequired(),
            EqualTo('password')
            
            ]
    )
    
