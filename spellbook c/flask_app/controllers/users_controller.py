from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

# ! ============LOGIN PAGE====RENDER====
@app.route("/")
def index():
    return render_template("index.html")


# ! ============REGISTER USER====POST====
@app.route("/users/register", methods=["post"])
def user_register():
    if not User.validate(request.form):
        return redirect("/")
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash,
    }

    user_id = User.create(data)
    session["user_id"] = user_id
    return redirect("/library")


# ! =============LOGIN USER====POST====
@app.route("/users/login", methods=["post"])
def login():
    data = {"email": request.form["email"]}
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("Invalid Email/Password")
        return redirect("/")
    session["user_id"] = user_in_db.id
    return redirect("/library")


# ! ===============LOGOUT USER/SESSION CLEAR====REDIRECT==========
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
