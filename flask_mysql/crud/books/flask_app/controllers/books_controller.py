from flask_app import app
from flask import Flask, render_template, redirect, request
from flask_app.models import authors_model, books_model, favorites_model

@app.route('/books')
def display_books():
    books = books_model.Book.get_all_books()
    print(books)
    return render_template('books.html', books=books)

@app.route('/books/<int:id>')
def display_single_book(id):
    book_data = {
        'id':id
    }
    book = books_model.Book.get_books_favorites(book_data)
    authors = authors_model.Author.get_all_authors()

    return render_template('book_show.html', book=book, authors=authors)

@app.route('/books/create', methods=['post'])
def create_book():
    book_data = {
        'title':request.form['book_title'],
        'num_of_pages':request.form['book_pages']
    }
    books_model.Book.books_create(book_data)
    return redirect('/books')

@app.route('/books/addfavorite', methods=['POST'])
def add_book_favorite():
    data = {
        'book_id':request.form['book_id'],
        'author_id':request.form['new_favorite']
    }
    book_id = request.form['book_id']
    print(book_id)
    favorites_model.Favorite.favorite_create(data)
    return redirect(f'/books/{book_id}')