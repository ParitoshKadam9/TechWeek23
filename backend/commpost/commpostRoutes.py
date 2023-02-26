from backend import app, api, db
from backend.commpost.commpostModel import Commpost 
from flask_restful import Resource 
from flask import jsonify, request, make_response

class allCommpost(Resource): 
    
    def get(self): 
        
        commposts = Commpost.query.all() 
        output = [] 
        
        for c in commposts: 
            cObj = {
                'id' : c.id, 
                'title' : c.title, 
                'value' : c.value, 
                'likes' : c.likes, 
                'created' : c.created, 
                'message' : c.message, 
                'to_uid' : c.to_uid, 
                'from_uid' : c.from_uid
            }
            output.append(cObj)
        
        return make_response(jsonify(output), 200) 

class commpostById(Resource): 
    
    def get(self, cid): 
        cps = Commpost.query.filter_by(cid = cid).first()
        
        cObj = {
            'id' : cps.id, 
            'title' : cps.title, 
            'value' : cps.value, 
            'likes' : cps.likes, 
            'created' : cps.created, 
            'message' : cps.message, 
            'to_uid' : cps.to_uid, 
            
        }