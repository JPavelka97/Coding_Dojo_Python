from flask import Flask
app = Flask(__name__)
app.secret_key = "login_and_registration"
DATABASE = 'recipes_db'