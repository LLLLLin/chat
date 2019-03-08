from flask import session
from flask_socketio import emit,join_room,leave_room
from .. import socketio


@socketio.on('joined', namespace='/chat')
def joined(message):
    print('debug', message)
    room = message.get('msg','')
    session['room'] = room
    join_room(room)
    emit('status',{'msg': session.get('name') + 'join the room.'}, room= room)

@socketio.on('text', namespace='/chat')
def text(message):
    room = message.get('room','')
    print('debug',room)
    emit('message',{'msg': session.get('name')+':'+message.get('msg')},room=room)

@socketio.on('left', namespace='/chat')
def left(message):
    room = session.get('room','')
    leave_room(room)
    emit('status',{'msg' : session.get('name')+ ':' + 'leave the room'}, room = room)