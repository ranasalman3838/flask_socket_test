from flask_restful import Resource
from api import app,socketio



class trigger_mdt_queries(Resource):
    def get(self):
        try:           
            updated_data = {'message': 'mdt table Queries has been changed!'}
            socketio.emit('mdt_queries_changed',updated_data)  
            return 'Socket message sent!'       
        except KeyError:
            return 'session is disconnected'
   

class trigger_shorages_dispute(Resource):
    def get(self):
        try:           
            updated_data = {'message': 'list_shortages Data has changed!'}
            socketio.emit('shortages_changed',updated_data,broadcast=True)
            return 'Socket message sent!'         
        except KeyError:
            return 'session is disconnected'
        
        # finally:
        #     # close the socket connection
        #     socketio.disconnect()

class trigger_mdt_table(Resource):
    def get(self):
        try:           
            updated_data = {'message': 'mdt table Data has been changed!'}
            socketio.emit('mdt_changed',updated_data,broadcast=True)
            return 'Socket message sent!'         
        except KeyError:
            return 'session is disconnected'