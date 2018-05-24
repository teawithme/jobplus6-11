#-*- coding:utf-8 -*-#

from flask import render_template,url_for,Blueprint

company = Blueprint('company', __name__, url_prefix='/company')

@company.route('/profile', methods=['GET', 'POST'])
def profile():
    form = CompanyProfile(obj=current_user)

