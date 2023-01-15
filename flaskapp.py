from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/flaskapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(280))
    user = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime)
    likes = db.Column(db.Integer, default=0)

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'))
    user = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime)


@app.route("/")
def index():
    return '<h3>This is the code for backend API, built to keep the record of likes on the messages</h3>'

#To create a new message:
@app.route('/message', methods=['POST'])
def create_message():
    data = request.get_json()
    message = Message(content=data['content'], user=data['user'], timestamp=datetime.datetime.now())
    db.session.add(message)
    db.session.commit()
    return jsonify({'message': 'Message created'}), 201

#To view a list of all messages:
@app.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return jsonify([message.serialize() for message in messages])

#To like a message:
@app.route('/like/<int:message_id>', methods=['POST'])
def create_like(message_id):
    data = request.get_json()
    like = Like(message_id=message_id, user=data['user'], timestamp=datetime.datetime.now())
    db.session.add(like)
    db.session.commit()
    message = Message.query.get(message_id)
    message.likes += 1
    db.session.commit()
    return jsonify({'message': 'Like created'}), 201
    
#To view the total number of likes for each message:
@app.route('/likes/<int:message_id>', methods=['GET'])
def get_likes(message_id):
    message = Message.query.get(message_id)
    return jsonify({'likes': message.likes})
