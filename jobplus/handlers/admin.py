# -*- coding:utf-8 -*-

from flask import Blueprint, render_template,url_for
#from flask_login import current_user
from jobplus.decorators import admin_required

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
@admin_required
def index():
    return render_template('admin/admin_base.html')
