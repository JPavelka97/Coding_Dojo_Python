from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/recipes')
def display_recipes():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id":session['user_id']
    }
    recipes = Recipe.get_all_recipes()
    user_name = User.get_by_id(data)
    return render_template('recipes.html', recipes=recipes, user_name=user_name)

@app.route('/recipes/<int:id>')
def display_single_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id':id
    }
    recipe = Recipe.get_one_recipe(data)
    user_name = User.get_by_id({"id":session['user_id']})
    return render_template('single_recipe.html', recipe = recipe, user_name=user_name)

@app.route('/recipes/new')
def display_create_recipe():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('recipes_new.html')

@app.route('/recipes/new/create', methods=['POST'])
def create_new_recipe():
    if not Recipe.validate(request.form):
        return redirect('/recipes/new')    
    data = {
        "name":request.form['name'],
        "description":request.form['description'],
        "instructions":request.form['instructions'],
        "date":request.form['date'],
        "under_30_minutes":request.form['under_30_minutes'],
        "users_id":session['user_id']
    }
    Recipe.add_new_recipe(data)
    return redirect('/recipes')

@app.route('/recipes/edit/<int:id>')
def display_edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id':id
    }
    recipe = Recipe.get_one_recipe(data)
    return render_template('recipes_edit.html', recipe=recipe, id=id)

@app.route('/recipes/edit/<int:id>/update', methods=["POST"])
def edit_recipe(id):
    if not Recipe.validate(request.form):
        return redirect(f'/recipes/edit/{id}')
    data = {
        "id":id,
        "name":request.form['name'],
        "description":request.form['description'],
        "instructions":request.form['instructions'],
        "date":request.form['date'],
        "under_30_minutes":request.form['under_30_minutes'],
        "users_id":session['user_id']
    }
    Recipe.edit_recipe(data)
    return redirect('/recipes')

@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    data={
        'id':id
    }
    Recipe.delete(data)
    return redirect('/recipes')