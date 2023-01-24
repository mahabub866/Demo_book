from sqlalchemy.dialects.postgresql import JSON
from db import db

class RBA(db.Model):
    __tablename__ = "roles"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    active=db.Column(db.Boolean,default=True)
    role = db.Column(JSON)
