from flask_app import app

# ALWAYS IMPORT CONTROLLERS
from flask_app.controllers import users_controller, recipes_controller
from flask_app.models import user_model, recipe_model

if __name__ == "__main__":
    app.run(debug=True)