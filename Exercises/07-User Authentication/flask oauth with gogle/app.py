from flask_dance.contrib.google import make_google_blueprint, google
from flask import Flask, redirect, url_for, render_template, session
import os
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = '1'
os.environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = '1'
#######################################################################
#######################################################################

app = Flask(__name__)


app.config['SECRET_KEY'] = 'mysecretkey'


blueprint = make_google_blueprint(
    client_id="1087212361449-cr65n94dmtpb8nvh4c78adbq5pgk7t4j.apps.googleusercontent.com", client_secret="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", offline=True, scope=["profile", "email"])
app.register_blueprint(blueprint, url_prefix="/login")


@app.route("/")
def index():
    return render_template("home.html")


@app.route('/welcome')
def welcome():
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email = resp.json()["email"]
    return render_template("welcome.html", email=email)


@app.route("/login/google")
def login():
    if not google.authorized:
        return render_template(url_for("google.login"))
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email = resp.json()["email"]
    return render_template("welcome.html", email=email)


if __name__ == "__main__":
    app.run()
