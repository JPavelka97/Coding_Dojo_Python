from flask_app import app
from flask_app.controllers import dojos_routes, ninjas_routes
from flask_app.models import ninja, dojo

if __name__ == "__main__":
    app.run(debug=True)