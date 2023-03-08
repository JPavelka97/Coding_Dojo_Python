from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#  =======LOGIN/REGISTER PAGE=========VIEW=========
@app.route('/')
def index():
    return render_template("index.html")

#  =======REGISTER==============ACTION/POST========
@app.route('/users/register', methods=['post'])
def user_register():
    if not User.validate(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name': request.form['f_name'],
        'last_name': request.form['l_name'],
        'email': request.form['email'],
        'password': pw_hash
    }

    user_id = User.create(data)
    session['user_id'] = user_id
    return redirect('/recipes')

@app.route('/users/login', methods=['post'])
def login():
    data = {"email" : request.form["email"]}
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash ('Invalid Email/Password')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash ('Invalid Email/Password')
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect("/recipes")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')