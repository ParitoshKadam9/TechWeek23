from backend import db
import datetime 
from sqlalchemy.sql import func 

class User(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    bits_id = db.Column(db.String(50))
    u_name = db.Column(db.String(50))
    pwd = db.Column(db.String(50)) 
    full_name = db.Column(db.String(100))
    email = db.Column(db.String(100)) 
    karma = db.Column(db.Integer(), default = 0)
    created = db.Column(db.DateTime(timezone = True), default = datetime.datetime.now)
    
    # child relations
    answer = db.relationship('Answer', backref = 'user', lazy = True)
    question = db.relationship('Question', backref = 'user', lazy = True)
    commpost = db.relationship('Commpost', backref = 'user', lazy = True)
    category = db.relationship('Category', backref = 'user', lazy = True)