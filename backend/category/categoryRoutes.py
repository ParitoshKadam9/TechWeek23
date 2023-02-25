import datetime
from backend import app, api, db
from backend.category.categoryModel import Category 
from flask_restful import Resource 
from flask import jsonify, request, make_response

class allCategories(Resource): 
    
    def get(self): 
        """Gets all categories"""
        cats = Category.query.all()
        output = [] 
        
        for c in cats: 
            cObj = {
                'id' : c.id, 
                'title' : c.title, 
                'description' : c.description, 
                'created' : c.created, 
                'uid' : c.uid
            }
            
            output.append(cObj) 

        return jsonify(output)
    
    def post(self): 
        """Creates a new category
        Body has to have : 'title', 'description', 'uid'"""
        data = request.get_json() 
        # TODO : implement login
        try: 
            cat = Category(
                title = data['title'], 
                description = data['description'], 
                created = datetime.datetime.now(),
                uid = data['uid']
            )
            
            db.session.add(cat) 
            db.session.commit() 
            cat = Category.query.filter_by(created = cat.created).first()
            cObj = {
                'id' : cat.id, 
                'title' : cat.title,
                'description' : cat.description, 
                'created' : cat.created, 
                'uid' : cat.uid,
            }
            return make_response(jsonify(cObj), 200) 
        
        except TypeError: 
            error = "You haven't provided all parameters"
            return make_response(jsonify({'error', error}), 301) 
    
    
class singleCategory(Resource): 
    
    def get(self, cid): 
        """
        Returns info on single category
        If category is not found returns > 300"""

        c = Category.query.filter_by(id = cid).first()
        if not c: 
            return make_response(jsonify({'error' : "Category doesn't exit"}), 301)
        cObj = {
            'id': c.id, 
            'title' : c.title, 
            'description' : c.description, 
            'created' : c.created, 
            'uid' : c.uid
        }
        return make_response(jsonify(cObj), 200) 

    def delete(self, cid): 
        """
        Deletes single category 
        If cat not found or some other error status > 300 """

        # TODO : implement login

        Category.query.filter_by(id = cid).delete() 
        db.session.commit()
        
        return 200

api.add_resource(allCategories, '/category') 
api.add_resource(singleCategory, '/category/<int:cid>')