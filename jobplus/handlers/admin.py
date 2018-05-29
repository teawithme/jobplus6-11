# -*- coding:utf-8 -*-

from flask import Blueprint, render_template,url_for,request, redirect, flash
#from flask_login import current_user
from jobplus.decorators import admin_required
from jobplus.models import User
from jobplus.forms import UserForm, RegisterForm

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
@admin_required
def index():
    return render_template('admin/admin_base.html')

@admin.route('/users')
@admin_required
def users():
    page = request.args.get('page', 1, type=int)
    pagination = User.query.paginate(
            page=page,
            per_page=20,
            error_out=False)
    return render_template('admin/users.html', pagination=pagination)

@admin.route('/users/adduser', methods=['GET','POST'])
@admin_required
def add_user():
    form = RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('success', 'success')
        return redirect(url_for('admin.users'))
    return render_template('admin/add_user.html', form=form)

@admin.route('/users/addcompany', methods=['GET','POST'])
@admin_required
def add_company():
    form = RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('success', 'success')
        return redirect(url_for('admin.users'))
    return render_template('admin/add_company.html', form=form)

@admin.route('/users/<int: user_id>/edituser',methods=['GET','POST'])
@admin_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    if user.is_company:
        form = CompanyEditForm(obj=user)
    else:
        form = UserEditForm(obj=user)
    if form.validate_on_submit():
        form.update(user)
        flash('success', 'success')
        return redirect(url_for('admin.users'))
    if user.is_company:
        form.url.data = user.company_detail.url
        form.desription = user.company_detail.description
    return render_template('admin/edit_user.html', form=form, user=user)
