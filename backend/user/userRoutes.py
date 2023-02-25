from backend import app, api, db
from backend.user.userModel import User 
from flask_restful import Resource 
from flask import jsonify, request, make_response

class allUsers(Resource): 
    
    def get(self): 
        """
        Returns all users in db as array 
        All pieces of information about the user are sent
        """
        users = User.query.all()
        output = [] 
        
        for user in users: 
            userObj = {
                'bits_id' : user.bits_id,
                'id' : user.id, 
                'u_name' : user.u_name, 
                'full_name' : user.full_name, 
                'email' : user.email, 
                'karma' : user.karma, 
                'created' : user.created
            }
            output.append(userObj)
        
        return jsonify(output) 
    
    def post(self): 
        """
        Adds a new user, verifys the information
        username && email shouldn't collide - response > 300
        body must have u_name, email, pwd, full_name
        """
        data = request.get_json()
        
        users = User.query.filter((User.bits_id == data['bits_id'])).first()

        if users: 
            error = 'User already exists'
            return make_response(jsonify({'error' : error}), 301)
        
        try: 
            user = User(
                    u_name = data['u_name'], 
                    pwd = data['pwd'], 
                    karma = 0, 
                    email = data['email'], 
                    full_name = data['full_name'], 
                    bits_id = data['bits_id'], 
                )
            db.session.add(user)
            db.session.commit()
            
            user = User.query.filter((User.bits_id == data['bits_id'])).first()
            userObj = {
                'bits_id' : user.bits_id,
                'id' : user.id, 
                'u_name' : user.u_name, 
                'full_name' : user.full_name, 
                'email' : user.email, 
                'karma' : user.karma, 
                'created' : user.created
            }
            return jsonify(userObj)

        except TypeError: 
                error = 'You have not provided all data necessary' 
                return make_response(jsonify({"error" : error}), 302) 

class singleUser(Resource): 
    
    def get(self, uid): 
        """
            Searches db for user and returns userobj 
            return status > 300 means error
        """
        #TODO: make login required 
        
        # u_name = request.headers.get('u_name')
        # pwd = request.headers.get('pwd') 
        user = User.query.filter_by(id = uid).first()

        if not user:
            return make_response(jsonify({'error' : 'User does not exit'}), 301) 
        
        filteredUser = {
            'id' : user.id, 
            'bits_id' : user.bits_id, 
            'u_name' : user.u_name, 
            'pwd' : user.pwd, 
            'full_name' : user.full_name, 
            'email' : user.email, 
            'karma' : user.karma, 
            'created' : user.created
        }
        
        return make_response(jsonify(filteredUser), 200) 
    
    def delete(self, uid): 
        """
        Deletes user with uid
        201 if user doesn't exist 
        301 if not logged in 
        """
        
        user = User.query.filter_by(id = uid) 
        if not user: 
            return make_response(jsonify({"error" : "User didn't exist"}), 201)

        User.query.filter_by(id = uid).delete()
        db.session.commit()
        
        return 200

api.add_resource(allUsers, '/user') 
api.add_resource(singleUser, '/user/<int:uid>') 
        
        
