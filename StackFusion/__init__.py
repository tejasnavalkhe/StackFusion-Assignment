from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from StackFusion.config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from StackFusion.main.views import main
    app.register_blueprint(main)

    return app
