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
    pass

class Job(Base):
    pass

class Company():
    pass
