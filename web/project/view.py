import flask
import datetime
from . import app, db
from . import forms, models

@app.route("/")
def homepage():
    ip = flask.request.remote_addr
    user = models.User.query.get(ip)

    if user is None:
        user = models.User(ip=ip)

        db.session.add(user)
        db.session.commit()

    if user.first_connect + datetime.timedelta(hours=1) > datetime.datetime.now():
        return flask.render_template("ban_msg.html")
    return flask.render_template("base.html")

@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    form = forms.Reg()
    if form.validate_on_submit():
        sum = form.money.data
        name = form.name.data
        print(name, sum)
    return flask.render_template("sign_up.html", form=form)





