from flask import Flask, jsonify, render_template, request
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
    name = db.Column(db.String(256))
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
    return render_template('home.html')


@app.route('/floor', methods=['GET'])
def floorlist():
    floors = Floor.query.all()
    return jsonify([{'id': f.id, 'number': f.number, 'image_file': f.image_file, 'info': f.info} for f in floors])


@app.route('/room', methods=['GET'])
def room_get():
    name = request.args.get('search')
    r = Room.query.filter_by(name=name).all()[0]
    return jsonify({'id': r.id, 'room_type': r.room_type, 'map_position_x': r.map_position_x,
                    'map_position_y': r.map_position_y,'capacity':r.capacity
                    } )


if __name__ == '__main__':
    app.run()
