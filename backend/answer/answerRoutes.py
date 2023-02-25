from backend import app, api, db
from backend.answer.answerModel import Answer 
from flask_restful import Resource 
from flask import jsonify, request, make_response

class allAnswers(Resource): 
    
    def get(self): 
        """
        Returns all answers
        All info about each answer
        """
        answers = Answer.query.all() 
        output = [] 
        
        for a in answers: 
            aObj = {
                'id' : a.id, 
                'value' : a.value, 
                'likes' : a.likes, 
                'created' : a.created
            }
            output.append(aObj) 

        return jsonify(output) 

class answersByQid(Resource): 
    
    def get(self, qid):
        """
        Seaches db for all answers whose qid = qid
        Returns array of qObj"""