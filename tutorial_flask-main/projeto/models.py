from main import db
from sqlalchemy.sql import func

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=True)
    creation_date = db.Column(db.DateTime, default=func.now())
    is_completed = db.Column(db.Boolean, default=False)
    completion_date = db.Column(db.DateTime, nullable=True)