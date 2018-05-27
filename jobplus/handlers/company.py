#-*- coding:UTF-8 -*-#

from flask import render_template,url_for,Blueprint,flash,redirect,request
from flask_login import login_required, current_user
from jobplus.models import User,Company
from jobplus.forms import CompanyForm

company = Blueprint('company', __name__, url_prefix='/company')

@company.route('/profile', methods=['GET', 'POST'])
def profile():
    if not current_user.is_company:
        flash('您不是企业用户！', 'warning')
        return redirect(url_for('front.index'))
    form = CompanyForm(obj=current_user.company)
    form.name.data = current_user.name
    form.email.data = current_user.email
    if form.validate_on_submit():
        form.update_profile(current_user)
        flash('企业信息更新成功', 'success')
        return redirect(url_for('front.index'))
    return render_template('company/profile.html', form=form)

@company.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = User.query.filter(User.role==User.ROLE_COMPANY).order_by(User.created_at.desc()).paginate(
            page=page,
            per_page=12,
            error_out=False
            )
    return render_template('company/index.html', pagination=pagination, active='company')
