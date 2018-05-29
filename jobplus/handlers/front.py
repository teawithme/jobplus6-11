from flask import Blueprint, redirect, url_for, render_template, flash
from jobplus.forms import LoginForm
from flask_login import login_user, login_required, logout_user
from jobplus.models import User

front=Blueprint('front',__name__)

@front.route('/')
def index():
    return render_template('index.html')

@front.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user, form.remember_me.data)
        if user.is_company:
            return redirect(url_for('company.profile'))
        else:
            return redirect(url_for('user.profile'))
    return render_template('login.html', form=form)

@front.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已经成功退出登录', 'success')
    return redirect(url_for('.index'))
