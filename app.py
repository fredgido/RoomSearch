from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'

db = SQLAlchemy(app)


class Floor(db.Model):
    __tablename__ = 'floor'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    image_file = db.Column(db.String(256))
    info = db.Column(db.Text)

    def __repr__(self):
        return repr(id)


class Room(db.Model):
    __tablename__ = 'room'
    id = db.Column(db.Integer, primary_key=True)
    map_position_x = db.Column(db.Float)
    map_position_y = db.Column(db.Float)
    room_type = db.Column(db.String(256))
    capacity = db.Column(db.Integer)
    schedule_file = db.Column(db.String(256))
    info = db.Column(db.Text)

    floor_id = db.Column(db.Integer, db.ForeignKey(Floor.id))

    def __repr__(self):
        return repr(id)


db.create_all()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/floor', methods=['GET'])
def floorlist():
    floors = Floor.query.all()
    return jsonify([{'id': f.id, 'number': f.number, 'image_file': f.image_file, 'info': f.info} for f in floors])


if __name__ == '__main__':
    app.run()
