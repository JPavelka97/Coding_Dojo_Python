from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app import app
from flask_app.models import books_model
import re

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []

# --------------------------------CREATE AUTHOR
    @classmethod
    def create_author(cls,data):
        query = """
        INSERT INTO authors (name) VALUES (%(name)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)

# ----------------------------------GET SINGLE AUTHOR & BOOKS
    @classmethod
    def get_author_books(cls,data):
        query = """
        SELECT * FROM authors LEFT JOIN favorites
        ON authors.id = favorites.author_id
        LEFT JOIN books ON favorites.book_id = books.id
        WHERE authors.id=%(id)s;
        """
        author_results = connectToMySQL(DATABASE).query_db(query,data)
        author = cls(author_results[0])
        list_of_books = []
        for book in author_results:
            book_data = {
                "id":book["books.id"],
                "title":book["title"],
                "num_of_pages":book["num_of_pages"],
                "created_at":book["books.created_at"],
                "updated_at":book["books.updated_at"]
            }
            list_of_books.append(books_model.Book(book_data))
        author.books = list_of_books
        print(author.books[0].title)
        return author

    @classmethod
    def get_one_author(cls,data):
        query = "SELECT * FROM authors WHERE id=%(id)s"
        author_info = connectToMySQL(DATABASE).query_db(query,data)
        if author_info:
            return cls(author_info[0])
        return False
# ---------------------------------GET ALL AUTHORS
    @classmethod
    def get_all_authors(cls):
        query = """
        SELECT * FROM authors;
        """
        authors = []
        author_results = connectToMySQL(DATABASE).query_db(query)
        if author_results:
            for author in author_results:
                authors.append(cls(author))
            return authors
        return False