from backend import db
import datetime 

class Commpost(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = True) 
    value = db.Column(db.String(200)) 
    likes = db.Column(db.Integer, default = 0)
    created = db.Column(db.DateTime(timezone = True), default = datetime.datetime.now())
    message = db.Column(db.Boolean, default = False)
    to_uid = db.Column(db.Integer, nullable = True)

    #parent relation
    cid = db.Column(db.Integer, db.ForeignKey('category.id'), nullable = False)
    from_uid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False) 
    
    