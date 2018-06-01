from flask import Blueprint, render_template, redirect, url_for, request, current_app
<<<<<<< HEAD
from jobplus.models import db, Job, User_job
=======
from jobplus.models import db, Job
>>>>>>> upstream/master
from flask_login import current_user
from jobplus.forms import LoginForm

job = Blueprint('job', __name__, url_prefix='/job')


@job.route('/')
def index():
    page = request.args.get('page', default=1, type=int)
    pagination = Job.query.paginate(
            page=page,
            per_page=current_app.config['INDEX_PER_PAGE'],
            error_out=False)
    return render_template('job/index.html', pagination=pagination)

@job.route('/<int:job_id>')
def detail(job_id):
    job = Job.query.get_or_404(job_id)
    return render_template('job/detail.html', job=job)

@job.route('/<int:job_id>/apply')
def apply(job_id):
    if current_user.is_authenticated:
<<<<<<< HEAD
        #job = Job.query.get_or_404(job_id)
        user_job = User_job(
                job_id=job_id,
                user_id=current_user.id
                )
        db.session.add(user_job)
        db.session.commit()
        return redirect(url_for('job.detail', job_id=job_id))
=======
        
        return render_template("job/detail.html", job=job)
>>>>>>> upstream/master
    else:
        form = LoginForm()
        return render_template("login.html", form=form)
