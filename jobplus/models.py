from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, 
            default=datetime.utcnow, 
            onupdate=datetime.utcnow)

class User(Base):
    __tablename__ = 'user'
    pass

class Job(Base):
    __tablename__ = 'job'
    pass

class Company():
    __tablename__ = 'company'
    pass
