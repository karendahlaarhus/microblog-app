import datetime
import dateutil.tz

from flask import Blueprint, render_template


from . import model

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    user1 = model.User(email="mary@example.com", name="mary")
    user2 = model.User(email="karen@example.com", name="karen")
    posts = [
        model.Message(
            user = user1, 
            text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum et ligula sed elit euismod auctor.", 
            timestamp = datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            user = user2, 
            text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum et ligula sed elit euismod auctor.", 
            timestamp = datetime.datetime.now(dateutil.tz.tzlocal())

        ),
    ]
    return render_template("main/index.html", posts=posts)

@bp.route("/profile")
def profile():
    user = model.User(email="erika@example.com", name="erika")
    posts = [
        model.Message(
            user = user, 
            text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum et ligula sed elit euismod auctor.", 
            timestamp = datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            user = user, 
            text = "Vestibulum et ligula sed elit euismod auctor.", 
            timestamp = datetime.datetime.now(dateutil.tz.tzlocal())
        ),
         model.Message(
            user = user, 
            text = "Lorem d auctor.", 
            timestamp = datetime.datetime.now(dateutil.tz.tzlocal())
        ),
    ]
    return render_template("main/user.html", user=user, posts=posts)

@bp.route("/message")
def message():
    user = model.User(email="test@example.com", name="Test User" )
    message = model.Message(user=user, text="Standard message", timestamp=datetime.datetime.now(dateutil.tz.tzlocal()))
    responses = [
         model.Message(
            user = user, 
            text = "Hei", 
            timestamp = datetime.datetime.now(dateutil.tz.tzlocal())
        ), 
        model.Message(
            user = user, 
            text = "På", 
            timestamp = datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            user = user, 
            text = "Deg", 
            timestamp = datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            user = user, 
            text = "Response",
            timestamp = datetime.datetime.now(dateutil.tz.tzlocal())
        ),
    ]
    return render_template("main/message.html", user=user, message=message, responses=responses )
