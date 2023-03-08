from flask_app import app
from flask import Flask, render_template, request, redirect
from flask_app.models.user import User

@app.route('/users')
def display_all():
    users = User.get_all_users()
    return render_template('index.html', all_users = users)

# Do I need a seperate route to render the page with the inputs?
@app.route('/users/new')
def display_create_page():
    return render_template('new_user.html')

# Added /create so it would run separately than /users/new
@app.route('/users/new/create', methods=['GET','POST'])
def new_user():
    data = {
        "first_name": request.form["f_name"],
        "last_name": request.form["l_name"],
        "email": request.form["email"]
    }
    User.add_new_user(data)
    return redirect('/users')

@app.route('/users/<int:id>')
def display_solo_user(id):
    data = {
        "id":id
    }
    user = User.display_single_user(data)
    return render_template('read_one.html', user=user)

@app.route('/users/<int:id>/edit')
def edit_solo_user(id):
    data = {
        "id":id
    }
    user = User.display_single_user(data)
    return render_template('edit.html', user=user)

@app.route('/users/<int:id>/edit/update', methods=['GET','POST'])
def update_solo_user(id):
    data = {
        "first_name": request.form["f_name"],
        "last_name": request.form["l_name"],
        "email": request.form["email"],
        "id":id
    }
    User.update_user(data)
    return redirect('/users/' + str(id))    

@app.route('/users/<int:id>/delete')
def delete_solo_user(id):
    data = {
    "id":id
    }
    User.delete_user(data)
    return redirect('/users')