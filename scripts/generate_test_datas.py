import os
import json
from random import randint
#from faker import Faker
from jobplus.models import db, User, Job, Company

#fake = Faker()


def iter_users():
    company = Company.query.filter_by(id=1).first()
    yield User(
        name='company1',
        username='ABC',
        email='abc@example.com',
        password='abcdefg',
        role=20,
        company=company
    )
    yield User(
        name='user1',
        username='Jack Lee',
        email='jacklee@example.com',
        password='protream',
        role=10
    )


def iter_companies():
    yield Company(
        location='Beijing',
        logo='test'
    )
        
def iter_jobs():
    company = Company.query.filter_by(id=1).first()
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


def run(): 
    for company in iter_companies():
        db.session.add(company)   
    
    for user in iter_users():
        db.session.add(user)

    for job in iter_jobs():
        db.session.add(job)


    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
