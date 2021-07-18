from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    create_date= db.Column(db.DateTime, default=datetime.utcnow)

def __init__(self, username, password):
    self.username = username
    self.password = password