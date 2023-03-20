from api import app,socketio

# RUN API
if __name__ == "__main__":   
   socketio.run(app,debug=True,port=5003)