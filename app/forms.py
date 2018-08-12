from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,Email

class LoginForm(FlaskForm):
    email=StringField('email',validators=[DataRequired(),Email()])
    pwd=PasswordField('pwd',validators=[DataRequired()])
    submit = SubmitField('登录')