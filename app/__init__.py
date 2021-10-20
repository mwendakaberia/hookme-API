import credentials
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema,fields

db=SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(credentials)
    #app.debug=True

    from user.register import register
    from user.login import login
    from user import settings

    app.register_blueprint(register)
    app.register_blueprint(login)
    app.register_blueprint(settings)

    db.init_app(app)

    return app