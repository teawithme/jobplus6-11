import os
import json
from random import randint
#from faker import Faker
from jobplus.models import db, User, Job, Company, User_job

#fake = Faker()


def iter_users():
    yield User(
        name='admin',
        username='admin',
        email='admin@jobplus.com',
        password='jobplus',
        role=30
    )
    yield User(
        name='ABC',
        username='company1',
        email='abc@example.com',
        password='abcdefg',
        role=20
    )
    yield User(
        name='Jack Lee',
        username='user1',
        email='jacklee@example.com',
        password='protream',
        role=10
    )
    yield User(
        name='Jack Ma',
        username='user2',
        email='jackma@example.com',
        password='taobao',
        role=10
    )


def iter_companies():
    user = User.query.filter_by(name='ABC').first()
    yield Company(
        location='Beijing',
        logo='test',
        user=user
    )
        
def iter_jobs():
    company = Company.query.order_by(Company.id).first()
    with open(os.path.join(os.path.dirname(__file__), '..', 'datas', 'jobs.json')) as f:
        jobs = json.load(f)
    for job in jobs:
        yield Job(
            title=job['title'],
            salary=job['salary'],
            location=job['location'],
            experience=job['experience'],
            company=company
        )

def iter_user_jobs():
    job = Job.query.order_by(Job.id).first()
    user = User.query.filter_by(username='user2').first()
    yield User_job(
        user_id=user.id,
        job_id=job.id
    )
 
def run(): 
    for user in iter_users():
        db.session.add(user)
    
    for company in iter_companies():
        db.session.add(company)   
    
    for job in iter_jobs():
        db.session.add(job)
    
    for user_job in iter_user_jobs():
        db.session.add(user_job)


    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
