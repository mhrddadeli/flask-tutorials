from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LogInForm


app = Flask(__name__)  # __name__ is a special variable name of the module
app.config["SECRET_KEY"] = "8a3a6b5c3e912fc5022cdcbad9a6ade2"
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
