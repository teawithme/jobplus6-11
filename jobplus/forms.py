from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,IntegerField,ValidationError
from wtforms.validators import Length, Email, Required, EqualTo, NumberRange, URL
from jobplus.models import db, User

class LoginForm(FlaskForm):
    email=StringField('email',validators=[Required(),Email()])
    password=PasswordField('passowrd',validators=[Required(),Length(6,24)])
    remember_me = BooleanField('remember_me')
    submit = SubmitField('submit') 

    def validate_email(self, field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱没有注册！')

    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if not user: #and not user.check_password(field.data):
            raise ValidationError('密码错误')

class UserForm(FlaskForm):
    name = StringField('姓名', validators=[Required(), Length(5, 32)])
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('重复密码', validators=[Required(), EqualTo('password')])
    mobile = IntegerField('手机号', validators=[Required(), NumberRange(min=11, message='无效的手机号')])
    work_year = IntegerField('工作年限', validators=[Required()])
    resume_url = StringField('简历链接', validators=[Required(), URL()])
    submit = SubmitField('提交')
    
    def update_user(self, user):
        self.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return user

class CompanyProfile(FlaskForm):
    pass
