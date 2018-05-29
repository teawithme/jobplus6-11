from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,IntegerField,ValidationError, SelectField
from wtforms.validators import Length, Email, Required, EqualTo, NumberRange, URL
from jobplus.models import db, User, Company

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
    username = StringField('Username', validators=[Required(), Length(5, 32)])
    name = StringField('姓名', validators=[Required(), Length(5, 32)])
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    mobile = IntegerField('手机号', validators=[Required(), NumberRange(min=11, message='无效的手机号')])
    work_year = IntegerField('工作年限', validators=[Required()])
    resume_url = StringField('简历链接', validators=[Required(), URL()])
    submit = SubmitField('提交')
    
    def add_user(self):
        user = User()
        self.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return user

    def update_user(self, user):
        self.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return user
    

class CompanyForm(FlaskForm):
    username = StringField('用户名', validators=[Required()])
    name = StringField('企业名称', validators=[Required()])
    email = StringField('企业邮箱', validators=[Required(), Email()])
    password = PasswordField('密码(不填则保持不变)')
    description = StringField('简要描述', validators=[Required(), Length(8,150)])
    location = StringField('企业地址', validators=[Required()])
    workers_num = SelectField('企业规模', choices=[('small','1~50'),('middle','51~100'),('big','101~200'), ('huge','200+')])
    logo = StringField('LOGO', validators=[Required(), URL()])
    field = StringField('公司领域', validators=[Required()])
    tags = StringField('公司技术标签(最多不超过十个，用空格隔开)', validators=[Required()])
    finance_stage = SelectField('融资进度', choices=[('p','初创企业'), ('a', '融资A轮'), ('b', '融资B轮'), ('c', '融资C轮'),('s','已上市')])
    welfares = StringField('公司福利(最多不超过十个，用空格隔开)', validators=[Required()])
    submit = SubmitField('提交')
    
    def add_company(self):
        company = Company()
        user = User()
        user.role = 20
        self.populate_obj(user)
        self.populate_obj(company)
        db.session.add(user)
        db.session.add(company)
        db.session.commit()
        return company
    
    def update_profile(self, user):
        user.name = self.name.data
        user.email = self.email.data
        
        #如果密码填写了就要改变密码
        if self.password.data:
            user.password = self.password.data

        #先判断公司数据是否是第一次建立
        if user.company:
            company = user.company
        else:
            company = Company()
            company.user_id = user.id
        self.populate_obj(obj=company)
        db.session.add(user)
        db.session.add(company)
        db.session.commit()

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[Required(), Length(3, 24)])
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('Repeat password', validators=[Required(), EqualTo('password')])
    submit = SubmitField('Submit')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('The name was registered')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('The email was registered')

    def create_user(self):
        user = User(username=self.username.data,
                    email=self.email.data,
                    password=self.password.data)
        db.session.add(user)
        db.session.commit()
        return user

        
