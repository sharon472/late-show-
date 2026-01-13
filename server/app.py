from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lateshow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Episode, Guest, Appearance


@app.route('/')
def home():
    return {"message": "Late Show API"}


# -----------------------
# GET /episodes
# -----------------------
@app.route('/episodes')
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([e.to_dict(only=("id", "date", "number")) for e in episodes])


# -----------------------
# GET /episodes/:id
# -----------------------
@app.route('/episodes/<int:id>')
def get_episode(id):
    episode = Episode.query.get(id)

    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    return jsonify(episode.to_dict())


# -----------------------
# DELETE /episodes/:id
# -----------------------
@app.route('/episodes/<int:id>', methods=["DELETE"])
def delete_episode(id):
    episode = Episode.query.get(id)

    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    db.session.delete(episode)
    db.session.commit()

    return jsonify({"message": "Episode deleted"}), 200


# -----------------------
# GET /guests
# -----------------------
@app.route('/guests')
def get_guests():
    guests = Guest.query.all()
    return jsonify([g.to_dict(only=("id", "name", "occupation")) for g in guests])


# -----------------------
# POST /appearances
# -----------------------
@app.route('/appearances', methods=["POST"])
def create_appearance():
    data = request.get_json()

    try:
        appearance = Appearance(
            rating=data["rating"],
            episode_id=data["episode_id"],
            guest_id=data["guest_id"]
        )

        db.session.add(appearance)
        db.session.commit()

        return jsonify(appearance.to_dict()), 201

    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400

