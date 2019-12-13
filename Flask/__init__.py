from flask import Flask
import Flask

from .models import db
from . import config

# This function is what we are going to use to create the flask app, hence the name 'create_app'
def create_app():
    flask_app = Flask(__name__)
    # This above line is what creates the flask application. it assigns a URI from the config.py file to the Flask app's
    # configuration. This URI is used to connect to the Postgres database.
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.app_context().push()
    db.init_app(flask_app) # This line links the database with the flask app
    db.create_all()
    return flask_app

