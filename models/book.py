from db import db
from sqlalchemy.types import JSON
import datetime
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.mutable import MutableList

class BookModel(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.Boolean)
    create_at=db.Column(db.DateTime, default=datetime.datetime.utcnow())
    book_info = db.Column(JSON)
    data = db.Column(MutableList.as_mutable(ARRAY(db.Integer)))
    
