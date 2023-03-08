from flask_app import app

# ALWAYS IMPORT CONTROLLERS and models necessary
from flask_app.controllers import authors_controller, books_controller
from flask_app.models.authors_model import Author
from flask_app.models.books_model import Book
# from flask_app.models import ***

if __name__ == "__main__":
    app.run(debug=True)