# -*- coding:utf-8 -*-

from flask import Blueprint, render_template,url_for,request
#from flask_login import current_user
from jobplus.decorators import admin_required
from jobplus.models import User

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
