
from sqlalchemy.dialects.postgresql import JSON
from db import db

class Example(db.Model):
    __tablename__ = "examples"
    
    id = db.Column(db.Integer, primary_key=True)
    json_column = db.Column(JSON)