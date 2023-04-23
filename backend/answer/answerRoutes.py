import datetime
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
                'created' : a.created, 
                'uid' : a.uid, 
                'qid' : a.qid
            }
            output.append(aObj) 

        return jsonify(output) 

class answersByQid(Resource): 
    
    def get(self, qid):
        """
        Seaches db for all answers whose qid = qid
        Returns array of aObj
        """
        answers = Answer.query.filter_by(qid = qid).all() 
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
    
    def post(self, qid): 
        """Adds new question
        Returns status > 300 if error 
        Body must have 'value', 'uid'
        """
        data = request.get_json() 

        try: 
            a = Answer(
                value = data['value'], 
                likes = 0, 
                uid = data['uid'], 
                qid = qid, 
                created = datetime.datetime.now(),
            )
            
            db.session.add(a) 
            db.session.commit() 
            
            a = Answer.query.filter_by(created = a.created).first()
            aObj = {
                'value' : a.value, 
                'uid' : a.uid, 
                'qid' : a.qid, 
                'created' : a.created, 
                'id' : a.id
            } 
            return make_response(jsonify(aObj), 200) 

        except TypeError: 
            error = "All parameters aren't provided"
            return make_response(jsonify({'error' : error}), 301) 
    
    def delete(self, qid):
        """Deletes all answers of question"""
        answers = Answer.query.filter_by(qid = qid).all() 
        
        for a in answers:
            Answer.query.filter_by(id = a.id).delete() 
            db.session.commit()
        
        return 200 

class singleAnswer(Resource): 
    
    def get(self, aid): 
        """Returns aObj for answer with id = aid
        Returns > 300 status if doesn't exist
        """
        a = Answer.query.filter_by(id = aid).first() 
        
        if not a: 
            return make_response(jsonify({'error' : "Given answer doesn't exit"}), 301)
        
        aObj = {
            'id' : a.id, 
            'value' : a.value, 
            'likes' : a.likes, 
            'created' : a.created, 
            'uid' : a.uid, 
            'qid' : a.qid
        }
        
        return make_response(jsonify(aObj), 200) 

    def delete(self, aid): 
        """
        Returns 200 if ok 
        201 if answer doesn't exist 
        """
        #TODO : make login required
        # u_name = request.headers.get('u_name')
        # pwd = request.headers.get('pwd')
        
        a = Answer.query.filter_by(id = aid).first()
        
        if not a: 
            return make_response(jsonify({'error' : "Answer doesn't exit"}), 201) 
        
        Answer.query.filter_by(id = aid).delete()
        db.session.commit() 
        return 200 

    def patch(self, aid): 
        """ 
        Return 200 ok if fine 
        301 if answer not found
        """
        # TODO : make logn required 
        data = request.get_json() 
        
        a = Answer.query.filter_by(id = aid).first()
        if not a: 
            return make_response(jsonify({'error' : 'answer not found'}), 301)
        try: 
            a.value = data['value']
        except TypeError: 
            pass 
        try: 
            a.likes = data['likes']
        except TypeError: 
            pass 
        
        db.session.commit()
        return 200 
    
api.add_resource(allAnswers, '/answer')
api.add_resource(answersByQid, '/<int:qid>/answer') 
api.add_resource(singleAnswer, '/answer/<int:aid>') 