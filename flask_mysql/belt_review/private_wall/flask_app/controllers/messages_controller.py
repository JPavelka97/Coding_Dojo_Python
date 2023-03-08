from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User
from flask_app.models.message_model import Message
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/dashboard')
def render_dashboard():
    users = User.get_all_users()
    print(users)
    user_id = {
            "user_id":session['user_id']
    }
    messages = (Message.get_user_messages(user_id))
    print(messages)
    return render_template('dashboard.html', users=users, messages=messages)

@app.route('/message/create', methods=['POST'])
def create_message():
    data = {
        "sender_id":request.form['sender_id'],
        "receiver_id":request.form['receiver_id'],
        "message":request.form['message']
    }
    Message.new_message(data)
    return redirect('/dashboard')