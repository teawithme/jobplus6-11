import json
from flask import Blueprint, render_template, request, current_app, redirect, url_for, flash
from jobplus.models import User
from jobplus.forms import UserForm
from flask_login import login_required, current_user

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/profile', methods=['GET', 'POST'])
def profile():
    user = User.query.get_or_404(current_user)
    form = UserForm(obj=user)
    if form.validate_on_submit():
        form.update_user(user)
        flash('个人信息更新成功', 'success')
        return redirect(url_for('user.profile'))
    return render_template('user/profile.html', form=form, user=user)


