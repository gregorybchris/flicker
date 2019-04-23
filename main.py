"""Flask app for the Flicker API."""

import settings

from flask import jsonify, request, Flask
from flask_cors import CORS, cross_origin
from models import Message, PhotoStat, SonicStat
from mongoengine import DoesNotExist, connect

app = Flask(__name__)

mongo_connection_format = ("mongodb://{}:{}@"
                           "cluster0-shard-00-00-6dexo.gcp.mongodb.net:27017,"
                           "cluster0-shard-00-01-6dexo.gcp.mongodb.net:27017,"
                           "cluster0-shard-00-02-6dexo.gcp.mongodb.net:27017"
                           "/flicker?ssl=true&replicaSet=Cluster0-shard-0"
                           "&authSource=admin&retryWrites=true")

connection_string = mongo_connection_format.format(
    settings.MONGO_USER, settings.MONGO_PASS)

CORS(app)
connect(settings.MONGO_DATABASE, host=connection_string)


def error(m, code):
    """Get error message."""
    return (jsonify(message=str(m)), code)


def validate_body(body, expected):
    if body is None:
        return error('request_body_not_found', 403)

    for param in expected:
        if param not in body:
            return error('missing_param_{}'.format(param), 403)


@app.route('/', methods=['GET'])
def hello():
    """Hello message."""
    return jsonify({
        'message': 'Welcome to Flicker API!',
        'version': '1.0.0',
        'endpoints': {
            '/message': {
                'method': 'POST',
                'params': ['message']
            },
            '/messages': {
                'method': 'GET',
                'params': []
            }
        }
    })


@app.route('/message', methods=['POST'])
def post_message():
    """
    Write a message to the DB.

    Request params:
        * message: STRING
    """
    body = request.get_json()
    validate_body(body, ['message'])

    text = body['message']
    message = Message(text=text)
    message.save()

    response = {'message': message.serialize()}
    return (jsonify(response), 200)


@app.route('/messages', methods=['GET'])
def get_messages():
    """Get a list of all messages in the DB."""
    messages = Message.objects()
    serialized = [m.serialize() for m in messages if m.enabled]
    response = {'messages': serialized}
    return (jsonify(response), 200)


@app.route('/photo', methods=['POST'])
def post_photo_stat():
    """
    Write a photo stat to the DB.

    Request params:
        * reading: FLOAT
    """
    body = request.get_json()
    validate_body(body, ['reading'])

    reading = body['reading']
    stat = PhotoStat(reading=reading)
    stat.save()

    response = {'stat': stat.serialize()}
    return (jsonify(response), 200)


@app.route('/photos', methods=['GET'])
def get_photo_stats():
    """Get a list of all photo stats in the DB."""
    stats = PhotoStat.objects()
    serialized = [m.serialize() for m in stats if m.enabled]
    response = {'stats': serialized}
    return (jsonify(response), 200)


@app.route('/sonic', methods=['POST'])
def post_sonic_stat():
    """
    Write a sonic stat to the DB.

    Request params:
        * reading: FLOAT
    """
    body = request.get_json()
    validate_body(body, ['reading'])

    reading = body['reading']
    stat = SonicStat(reading=reading)
    stat.save()

    response = {'stat': stat.serialize()}
    return (jsonify(response), 200)


@app.route('/sonics', methods=['GET'])
def get_sonic_stats():
    """Get a list of all sonic stats in the DB."""
    stats = SonicStat.objects()
    serialized = [m.serialize() for m in stats if m.enabled]
    response = {'stats': serialized}
    return (jsonify(response), 200)
