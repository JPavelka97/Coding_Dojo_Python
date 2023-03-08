from flask_app import app
from flask import Flask, render_template, request, redirect
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def display_dojos():
    dojos = Dojo.get_all_dojos()
    return render_template('dojos.html', dojos=dojos)

@app.route('/dojo/new', methods=['POST'])
def new_dojo():
    data = {
        "name": request.form['dojo_name']
    }
    Dojo.add_new_dojo(data)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def display_single_dojo(id):
    dojo_data = {
        "id":id
    }
    dojo = Dojo.retrieve_all_ninjas_in_dojo(dojo_data)
    return render_template('dojo_display.html', dojo=dojo)
