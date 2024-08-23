from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from forms import RegistrationForm, LogInForm


app = Flask(__name__)  # __name__ is a special variable name of the module
app.config["SECRET_KEY"] = "8a3a6b5c3e912fc5022cdcbad9a6ade2"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)1
    email = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


posts = [
    {
        "title": "Post 1",
        "content": "This is the first post",
        "author": "John Doe",
        "date_posted": "April 1, 2016",
    },
    {
        "title": "Post 2",
        "content": "This is the second post",
        "author": "jackson Doe",
        "date_posted": "April 1, 2016",
    },
]


@app.route("/")  # decorators add extra functionality to an existing function
@app.route("/home")
def home_page():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about_page():
    return render_template("about.html", title="About Us")


@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(
            f"Account Created for {form.username.data}!",
            "success",
        )
        return redirect(url_for("home_page"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LogInForm()
    if form.validate_on_submit():
        if form.email.data == "mhrddadeli@gmail.com" and form.password.data == "1234":
            flash("You Are Logged In", "success")
            return redirect(url_for("home_page"))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Log In", form=form)


# run directy from the file
if __name__ == "__main__":
    app.run(debug=True)
