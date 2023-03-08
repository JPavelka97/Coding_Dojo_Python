from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models import user_model
from flask_app.controllers import email_controllers


if __name__=="__main__":   
    app.run(debug=True)    