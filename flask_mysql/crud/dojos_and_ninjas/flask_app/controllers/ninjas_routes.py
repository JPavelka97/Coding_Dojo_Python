from flask_app import app
from flask import Flask, render_template, request, redirect
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas/new', methods=['GET','POST'])
def new_ninja():
    data = {
        "first_name": request.form['f_name'],
        "last_name": request.form['l_name'],
        "age": request.form['age'],
        "dojo_id": request.form['dojo_id']
    }
    dojo_id=request.form['dojo_id']
    Ninja.add_new_ninja(data)
    return redirect(f'/dojos/{dojo_id}')

@app.route('/ninjas')
def render_create_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template('ninja_create.html', dojos=dojos)
