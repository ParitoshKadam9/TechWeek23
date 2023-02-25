from backend import db
import datetime
from sqlalchemy.sql import func 

class Question(db.Model): 
    id = db.Column(db.Integer, primary_key = True) 
    title = db.Column(db.String(100))
    value = db.Column(db.String(200))
    likes = db.Column(db.Integer, default = 0) 
    created = db.Column(db.DateTime(timezone = True), default = datetime.datetime.now) 

    # parent relations
    uid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    cid = db.Column(db.Integer, db.ForeignKey('category.id'), nullable = False)
    
    #child relations
    answer = db.relationship('Answer', backref = 'question', lazy = True)
    