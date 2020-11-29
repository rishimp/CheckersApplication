from flask import Flask
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)


@socketio.on('my event')
def handle_message(message):
    #print("Recieved Message " + str(message))
    print("test")

# serves the index page
@app.route('/')
def index():
    return serve_file('index.html')

@app.route('/test/<user>')
def hello_world1(user):
    return user


# returns the text from a file
def serve_file(filename):
    file = open(filename, mode='r')
    file_text = file.read()
    file.close()
    return file_text