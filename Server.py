from flask import Flask
from flask_socketio import SocketIO, join_room, leave_room, send, emit
from .game import Game
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)

rooms = {}
room_games = {}
room_ready = {}

@socketio.on('start game')
def start_game(username, room):
    """[Starts the game with the username and the room entered]

    Args:
        username (string): [the name of the user starting the game]
        room (string): [the name of the user in which the user wants to start the game]
    """
    #print("starting game for " + username)
    if room not in room_ready.keys():
        room_ready[room] = [username]
    elif username not in room_ready[room]:
        room_ready[room].append(username)
    if len(room_ready[room]) == 2:
        coin = random.randint(0,1)
        room_games[room] = Game(rooms[room][coin], rooms[room][1-coin])
        del room_ready[room]
        emit("board update", room_games[room].get_board(), room=room)

@socketio.on('join room')
def join_game(username, room):
    """[joins the game with the room name]

    Args:
        username (string): [the name of the user entering the room]
        room (string): [the name of the room the user wants to enter]
    """
    print("joining room " +  room + " " + username)
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
    emit_room_update(room)


@socketio.on('leave room')
def leave_game(username, room):
    """[the user leaves the room they ar ein]

    Args:
        username (string): [the name of the user that wants to leave]
        room (string): [the room the user wants to exit]
    """
    if room not in rooms.keys():
        print("Room is not in use")
    elif username in rooms[room]:
        rooms[room].remove(username)
        leave_room(room)
        if len(rooms[room]) == 0:
            del rooms[room]
    emit_room_update(room)

def emit_room_update(room):
    """[updates the users of the room]

    Args:
        room (string): [the room name we are updating]
    """
    if len(rooms[room]) == 0:
        emit('room update', {"user1" : "", "user2" : "", "room" : room}, room=room)
    elif len(rooms[room]) == 1:
        emit('room update', {"user1" : rooms[room][0], "user2" : "", "room" : room}, room=room)
    elif len(rooms[room]) == 2:
        emit('room update', {"user1" : rooms[room][0], "user2" : rooms[room][1], "room" : room}, room=room)

@socketio.on('piece clicked')
def piece_clicked(username, room, piece_id):
    """[highlits the piece the user clicks]

    Args:
        username ([string]): [the name of user clicking the piece]
        room ([stirng]): [the name of the room in which the pieve is clicked]
        piece_id ([int]): [the int assigned to the piece]
    """
    x_str, y_str, color = piece_id.split(',')
    x0 = int(x_str)
    y0 = int(y_str)
    if room_games[room].is_correct_side(username, color):
        room_games[room].set_tentative_selection(x0, y0)
        room_games[room].highlight_possible_moves(username, x0, y0)
        emit('board update', room_games[room].get_board(), room=room)

@socketio.on('space clicked')
def space_clicked(username, room, piece_id):
    """[if a space is clicked by the user for a piece]

    Args:
        username ([type]): [description]
        room ([type]): [description]
        piece_id ([type]): [description]
    """
    x_str, y_str = piece_id.split(',')
    x1 = int(x_str)
    y1 = int(y_str)
    room_games[room].make_move(username, x1, y1)
    emit('board update', room_games[room].get_unhighlighted_board(), room=room)


@socketio.on('draw game')
def draw_game(username, room):
    # example of how to emit a message
    emit("draw", username, room=room)

@socketio.on('forfeit game')
def forfeit_game(username, room):
    pass # do nothing for now

# serves the index page
@app.route('/')
def index():
    return serve_file('index.html')

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