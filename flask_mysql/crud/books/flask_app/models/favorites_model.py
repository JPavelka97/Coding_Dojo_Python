from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app import app
from flask_app.models import books_model, authors_model

class Favorite:
    def __init__(self,data):
        self.author_id=data['author_id']
        self.book_id=data['book_id']

    @classmethod
    def favorite_create(cls,data):
        query = """
        INSERT INTO favorites (book_id,author_id) 
        VALUES (%(book_id)s,%(author_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)