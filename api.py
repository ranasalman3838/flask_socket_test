#imports
from flask import Flask
from flask_restful import Api
from flask_socketio import SocketIO,emit
#Flask app, api creation
from flask_cors import CORS


app = Flask(__name__,template_folder='Email_Templates')
api = Api(app)
CORS(app)
socketio = SocketIO(app, async_mode='eventlet',cors_allowed_origins='*')

#API ROUTES IMPORT

from main import *

#socket triger events for change in data 
api.add_resource(trigger_mdt_queries,"/trigerMDT")
api.add_resource(trigger_shorages_dispute,"/trigerShortagesDispute")
api.add_resource(trigger_mdt_table,"/trigerTable")