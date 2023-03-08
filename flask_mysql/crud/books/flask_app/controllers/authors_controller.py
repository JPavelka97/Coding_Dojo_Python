from flask_app import app
from flask import Flask, render_template, redirect, request
from flask_app.models import authors_model, books_model, favorites_model

@app.route('/authors')
def display_authors():
    authors = authors_model.Author.get_all_authors()
    return render_template('authors.html', authors=authors)

@app.route('/authors/<int:id>')
def display_single_author(id):
    author_data = {
        "id":id
    }
    author = authors_model.Author.get_author_books(author_data)
    books = books_model.Book.get_all_books()
    return render_template('author_show.html', author=author, books=books)

@app.route('/authors/create', methods=['POST'])
def create_author():
    author_data = {
        'name':request.form['author_name']
    }
    authors_model.Author.create_author(author_data)
    return redirect('/authors')

@app.route('/authors/addfavorite', methods=['POST'])
def add_author_favorite():
    data = {
        'book_id':request.form['book'],
        'author_id':request.form['author_id']
    }
    author_id = request.form['author_id']
    favorites_model.Favorite.favorite_create(data)
    return redirect(f'/authors/{author_id}')