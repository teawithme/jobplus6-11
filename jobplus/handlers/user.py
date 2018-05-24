#-*- coding:utf-8 -*-#

import json
from flask import Blueprint, render_template, request, current_app, redirect, url_for, flash
from jobplus.models import User
from jobplus.forms import UserForm
from flask_login import login_required, current_user

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/profile', methods=['GET', 'POST'])
def profile():
    #get_or_404()里面的参数应该是可迭代对象
    user = current_user           #User.query.get_or_404(current_user)
    form = UserForm(obj=user)
    if form.validate_on_submit():
        form.update_user(user)
        #汉字提交出现编码错误
        flash('Personal information update successfully', 'success')
        #提交以后应该返回主页
        return redirect(url_for('front.index'))
    return render_template('user/profile.html', form=form, user=user)


