from flask_app import app
from flask_app.controllers import messages_controller,users_controller

# ALWAYS IMPORT CONTROLLERS and models necessary
# from flask_app.controllers import ***
# from flask_app.models import ***
# make sure to instantiate in joins

if __name__ == "__main__":
    app.run(debug=True)