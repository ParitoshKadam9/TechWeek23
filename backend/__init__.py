from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api 
from flask_cors import CORS
from functools import wraps 
import jwt 

app = Flask(__name__, instance_relative_config = True)
app.config.from_object('backend.config.DefaultConfig')
app.secret_key = 'secret_key' 

CORS(
    app, 
    supports_credentials = True, 
    allow_headers = '*'
)

api = Api(app) 

db = SQLAlchemy(app) 

#importing api routes
from backend.user import userRoutes

#importing models 
from backend.user.userModel import User