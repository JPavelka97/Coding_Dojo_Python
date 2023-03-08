from flask import Flask
app = Flask(__name__)
app.secret_key = "wall"
DATABASE = 'wall_db'