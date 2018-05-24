from flask import url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, 
            default=datetime.utcnow, 
            onupdate=datetime.utcnow)


class User(Base, UserMixin):
    __tablename__ = 'user'
    

    ROLE_USER = 10
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True, nullable=False)
    name = db.Column(db.String(32), index=True, nullable=False)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    _password = db.Column('password', db.String(256), nullable=False)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    work_year = db.Column(db.Integer)
    mobile = db.Column(db.Integer, unique=True)
    resume_url = db.Column(db.String(256), unique=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id', ondelete='CASCADE'))
    company = db.relationship('Company')
    
    
    def __repr__(self):
        return '<User:{}>'.format(self.username)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, orig_password):
        self._password = generate_password_hash(orig_password)

    def check_password(self, password):
        return check_password_hash(self._password, password)

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    @property
    def is_company(self):
        return self.role == self.ROLE_COMPANY


class Job(Base):
    __tablename__ = 'job'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id', ondelete='CASCADE'))
    company = db.relationship('Company', uselist=False)

    @property
    def url(self):
        return url_for('company.job', company_id=self.company.id, job_id=self.id)

    def __repr__(self):
        return '<Job:{}>'.format(self.name)

class Company(Base):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False) 
    description = db.Column(db.String(256))
    city = db.Column(db.String(64), nullable=False)
    scale = db.Column(db.String(64))
    workers_num = db.Column(db.String(32))
    user = db.relationship('User')
    jobs = db.relationship('Job')

    @property
    def url(self):
        return url_for('company.index', company_id=self.id)

    def __repr__(self):
        return '<Company:{}>'.format(self.name)

class Jobhunter(User):
    pass
