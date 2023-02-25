from backend import db
import datetime 

class Answer(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    value = db.Column(db.String(200)) 
    likes = db.Column(db.Integer, default = 0) 
    created = db.Column(db.DateTime(timezone = True), default = datetime.datetime.now) 
    
    #parent relations
    uid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False )
    qid = db.Column(db.Integer, db.ForeignKey('question.id'), nullable = False)

    #child relations 
    