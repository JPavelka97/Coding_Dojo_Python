from flask_app import app
from flask_app.controllers import spells_controlller, users_controller
from flask_app.models import spell_model, user_model
# ALWAYS IMPORT CONTROLLERS and models necessary
# from flask_app.controllers import ***
# from flask_app.models import ***


if __name__ == "__main__":
    app.run(debug=True)