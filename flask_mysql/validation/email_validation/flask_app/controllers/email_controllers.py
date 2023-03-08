from flask_app import app
from flask import Flask, render_template, request, redirect
from flask_app.models.user_model import User

@app.route('/')
def display_index():
    return render_template("index.html")


@app.route('/create', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect ('/')
    User.create(request.form)
    return redirect ('/display')

@app.route('/display')
def display_results():
    emails = User.get_all()
    print(emails)
    return render_template('display.html', emails=emails)
