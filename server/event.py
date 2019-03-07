from flask import session
from flask_socketio import emit,join_room,leave_room
from app import socketio

@socketio.on('joined', namespace='/chat')
def joined(message):
    room = message.get('msg','')
    print('debug', room)
    join_room(room)
    emit('status',{'msg': session.get('name') + 'join the room.'}, room= room)

@socketio.on('text', namespace='/chat')
def text(message):
    room = message.get('room','')
    print('debug',room)
    emit('message',{'msg': message.get('msg')},room=room)

@socketio.on('left', namespace='/chat')
def left(message):
    leave_room()
    emit('status',{'msg' : session.get('name')+ ':' + 'leave the room'})