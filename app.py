import settings

from flask import jsonify, request, Flask
from models import Message, LightStat
from mongoengine import DoesNotExist, connect
from flask_cors import CORS, cross_origin


app = Flask(__name__)

connection_string = "mongodb+srv://{}:{}@{}.mongodb.net".format(
    settings.MONGO_USER, settings.MONGO_PASS, settings.MONGO_CLUSTER)

CORS(app)
connect(settings.MONGO_DATABASE, host=connection_string)


# message = Message(text="Hello, this is a message")
# message.save()

stat = LightStat(reading=1.85)
stat.save()
