from flask import Flask, render_template, request, redirect, session
from flask_app.models import form_model
from flask_app.controllers import form_controller
app = Flask(__name__)  
app.secret_key = 'dojo_survey'


if __name__=="__main__":   
    app.run(debug=True)    