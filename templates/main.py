from flask import Flask, render_template, redirect, url_for

__winc_id__ = '9263bbfddbeb4a0397de231a1e33240a'
__human_name__ = 'templates'

app = Flask(__name__)


@app.route('/')
def index():
    title = "Home"
    return render_template("index.html", title=title)

@app.route("/home")
def home():
    return redirect(url_for("index"))

@app.route("/about")
def about():
    title = "About"
    return render_template("about.html", title=title)

@app.route("/user")
def user():
    user = "Jochum"
    return render_template("user.html", title=user, name=user)

if __name__ == "__main__":
    app.run(debug=True)
