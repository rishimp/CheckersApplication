from flask import Flask
from flask_socketio import SocketIO, join_room, leave_room, send, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)

# @socketio.on('connect')
# def test_connect():
#     emit('my response', {'data': 'Connected'})
#
# @socketio.on('disconnect')
# def test_disconnect():
#     print('Client disconnected')


rooms = {}
room_games = {}

@socketio.on('start game')
def start_game(username, room):
    print(username, room)


@socketio.on('join room')
def join_game(username, room):
    print(username, room)

    if not is_valid_username(username, room):
        print("Invalid Username")
    elif not is_valid_room(room):
        print("Invalid Room")
    elif room not in rooms.keys():
        rooms[room] = [username]
        join_room(room)
    else:
        if len(rooms[room]) == 1:
            rooms[room].append(username)
            join_room(room)
    print(rooms)


@socketio.on('leave room')
def leave_game(username, room):
    print(username, room)
    if room not in rooms.keys():
        print("Room is not in use")
    elif username in rooms[room]:
        rooms[room].remove(username)
        leave_room(room)
        if len(rooms[room]) == 0:
            del rooms[room]
    print(rooms)


@socketio.on('piece clicked')
def piece_clicked(username, room, piece_id):
    x_str, y_str = piece_id.split(',')
    x0 = int(x_str)
    y0 = int(y_str)
    # get highlighted moves from here


@socketio.on('draw game')
def draw_game(username, room):
    print(username, room)
    # example of how to emit a message
    emit("draw", username, room=room)

@socketio.on('forfeit game')
def forfeit_game(username, room):
    print(username, room)


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

def is_valid_username(username, room):
    if username == "":
        return False
    elif room not in rooms.keys():
        return True
    elif username in rooms[room]:
        return False
    else:
        return True

def is_valid_room(room):
    if room == "":
        return False
    return True