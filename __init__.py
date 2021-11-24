from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = b"\x8c\xa5\x04\xb3\x8f\xa1<\xef\x9bY\xca/*\xff\x12\xfb"
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://microblog:waDBlog@localhost/Microblog"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from . import main
    app.register_blueprint(main.bp)
    from . import auth
    app.register_blueprint(auth.bp)
    return app
