from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length, Email, Required

class LoginForm(FlaskForm):
	email=StringField('email',validators=[Required(),Email()])
	password=PasswordField('passowrd',validators=[Required(),Length(6,24)])
	remember_me = BooleanField('remember_me')
    submit = SubmitField('submit') 

    def validate_email():
    	pass
    def validate_password():
    	pass
