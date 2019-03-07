from flask import Flask
from flask_socketio import SocketIO
from server.routes import main as index_route
app = Flask(__name__)

app.register_blueprint(index_route)
from  server import event
app.config['SECRET_KEY'] = 'hklsdhflidash'
app.debug = True
socketio = SocketIO(app)
if __name__ == '__main__':
    config ={
        'debug': True,
        'host':'localhost',
        'port': 5000,
    }
    socketio.run(app)