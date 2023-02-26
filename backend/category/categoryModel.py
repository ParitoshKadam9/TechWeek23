from backend import db
import datetime

class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True) 
    title = db.Column(db.String(50)) 
    description = db.Column(db.String(200))
    created = db.Column(db.DateTime(timezone = True), default = datetime.datetime.now)

    #parent 
    uid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False) 
    
    #child
    # commpost = db.relationship('Commpost', backref = 'category', lazy = True) 
 