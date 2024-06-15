from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    DateField,
    PasswordField,
    SubmitField,
    BooleanField
)

from wtforms.validators import (
    DataRequired,
    Email,
    Length,
    Optional,
    EqualTo
)


class SignupForm(FlaskForm):
    
    username = StringField(
        'Username',
        validators=[DataRequired(),Length(min=4, max=25)]
        )

    email=StringField(
        "email",
        validators=[DataRequired(),Email()]
    )

    gender = SelectField(
        "Gender",
        choices=["Male","Female","Other"],
        validators=[Optional()]
    )

    dob=DateField(
        "date of birth",
        validators=[Optional()]
    )

    password=PasswordField(
        "password",
        validators=[DataRequired(),Length(5,25)]
    )

    cnfrm_password=PasswordField(
        "cnfrm_password",
        validators=[DataRequired(),Length(5,25),EqualTo("password")]
    )

    submit=SubmitField("sign up")



class LoginForm(FlaskForm):
    email=StringField(
        "email",
        validators=[DataRequired(),Email()]
        )
    password=PasswordField(
        "password",
        validators=[DataRequired(),Length(5,25)]
    )
    remember_me = BooleanField("remember me")
    login=SubmitField("login")
    