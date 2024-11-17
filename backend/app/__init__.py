from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    db.init_app(app)
    CORS(app)

    from .routes import app as routes_blueprint
    app.register_blueprint(routes_blueprint)

    return app
