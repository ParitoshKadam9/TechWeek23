from backend import app, api, db
from backend.question.questionModel import Question 
from flask_restful import Resource 
from flask import jsonify, request, make_response

class allQuestions(Resource):
    
    def get(self): 
        """
        Returns all questions
        All info about
        """
        questions = Question.query.all()
        output = [] 
        
        for q in questions: 
            qObj = {
                'id' : q.id, 
                'value' : q.value,
                'likes' : q.likes, 
                'created' : q.created, 
                'title' : q.title
            }
            output.append(qObj) 
            
        return jsonify(output)

    

class questionsByCid(Resource): 
    
    def get(self, cid):
        """
        Searches db for all questions whose cid == cid
        Returns the qObj
        """

        questions = Question.query.filter((Question.cid == cid)).all() 
        output = []
        for q in questions: 
            qObj = {
                'id' : q.id, 
                'title' : q.title, 
                'value' : q.value, 
                'likes' : q.likes, 
                'created' : q.created
            }
            output.append(qObj)
        
        return jsonify(output) 
    
    def post(self, cid): 
        """
        Adds a new question
        Returns status > 300 if error
        body must have 'value', 'title', 'uid', 'cid'
        """
        data = request.get_json() 
        
        try : 
            question = Question(
                value = data['value'], 
                title = data['title'], 
                likes = 0, 
                uid = data['uid'], 
                cid = cid
            )
            
            db.session.add(question) 
            db.session.commit() 
            
            question = Question.query.filter((Question.value == data['value'])).first() 
            qObj = {
                'id' : question.id, 
                'title' : question.title, 
                'value' : question.value, 
                'likes' : question.likes, 
                'created' : question.created,
                'uid' : question.uid, 
                'cid' : cid
            }
            return make_response(jsonify(qObj), 200) 

        except TypeError: 
            error = "You haven't provided all necessary data"
            return make_response(jsonify({'error' : error}), 301)
    
    def delete(self, cid): 
        """
        Deletes all questions of certain community
        """
        questions = Question.query.filter((Question.cid == cid)).all()
        
        for q in questions: 
            Question.query.filter_by(id = q.id).delete()
            db.session.commit() 
        
        return 200
    
class singleQuestion(Resource): 
    
    def get(self, qid): 
        """
        Returns qObj for the question with id = qid
        Returns > 300 status if doesn't exist
        """ 
        #TODO: make login required 

        # u_name = request.headers.get('u_name')
        # pwd = request.headers.get('pwd')
        
        q = Question.query.filter_by(id = qid).first()
        
        if not q: 
            return make_response(jsonify({"error" : 'Question does not exit'}), 301)    
        
        filQues = {
            'id' : q.id, 
            'title' : q.title, 
            'value' : q.value, 
            'likes' : q.likes, 
            'created' : q.created, 
            'uid' : q.uid, 
            'cid' : q.cid
        }
        
        return make_response(jsonify(filQues), 200)
    
    def delete(self, qid): 
        """ 
        Returns 200 ok if fine
        Returns 201 if question didn't exist
        """
        #TODO : make login required
        
        # u_name = request.headers.get('u_name')
        # pwd = request.headers.get('pwd')
        
        q = Question.query.filter(Question.id == qid).first() 
        
        if not q: 
            return make_response(jsonify({'error' : 'Question did not exist'}), 201) 
        
        Question.query.filter_by(id = qid).delete()
        db.session.commit()
        
        return 200

    def patch(self, qid): 
        """
        Returns 200 ok if fine 
            301 if question not found 
            302 if data given incorrect/unfilled
        Reqires 'title', 'value', 'likes' to be passed
        (if field is empty)
        """
        data = request.get_json()
        
        question = Question.query.fiter((Question.id == qid)).first() 
        if not question: 
            return make_response(jsonify({'error' : 'Question does not exit'}), 301)
        try: 
            question.title = data['title']
        except TypeError: 
            pass 
        try: 
            question.value = data['value'] 
        except TypeError:
            pass 
        try: 
            question.likes = data['likes'] 
        except TypeError: 
            pass 
        
        return 200 


api.add_resource(allQuestions, '/question') 
api.add_resource(questionsByCid, '/<int:cid>/question')
api.add_resource(singleQuestion, '/question/<int:qid>')