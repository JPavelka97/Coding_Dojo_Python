from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app import app
from flask_app.models import authors_model

class Book:
    def __init__(self,data):
        self.id=data["id"]
        self.title=data["title"]
        self.num_of_pages=data["num_of_pages"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]

    @classmethod
    def get_all_books(cls):
        query = """
        SELECT * FROM books;
        """
        books = []
        book_results = connectToMySQL(DATABASE).query_db(query)
        if book_results:
            for book in book_results:
                books.append(cls(book))
            return books
        return False

    @classmethod
    def get_one_book(cls,id):
        query = """
        SELECT * FROM books
        WHERE id=%(id)s;
        """
        book_info = connectToMySQL(DATABASE).query_db(query,id)
        if book_info:
            return cls(book_info[0])
        return False

    @classmethod
    def get_books_favorites(cls,data):
        query = """
        SELECT * FROM books JOIN favorites
        ON books.id=favorites.book_id
        JOIN authors ON favorites.author_id=authors.id
        WHERE books.id = %(id)s;
        """
        book_results = connectToMySQL(DATABASE).query_db(query,data)
        book = cls(book_results[0])
        book_authors = []
        for author in book_results:
            author_data = {
                "id":author["authors.id"],
                "name":author["name"],
                "created_at":author["authors.created_at"],
                "updated_at":author["authors.updated_at"]
            }
            book_authors.append(authors_model.Author(author_data))
        print(book_authors)
        book.authors = book_authors
        return book

    @classmethod
    def add_book_favorites(cls,data):
        query = """
        INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data) 

    @classmethod
    def books_create(cls,data):
        query = """
        INSERT INTO books (title,num_of_pages) VALUES (%(title)s,%(num_of_pages)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)        
    
