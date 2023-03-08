from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app import app
from flask_app.models import user_model
from flask import flash
from flask_bcrypt import Bcrypt
import re

class Recipe:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.description=data['description']
        self.instructions=data['instructions']
        self.under_30_minutes=data['under_30_minutes']
        self.date_made=data['date_made']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.users_id=data['users_id']

    @classmethod
    def get_one_recipe(cls,data):
        query = """
        SELECT * FROM recipes 
        JOIN users ON recipes.users_id=users.id 
        WHERE recipes.id=%(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query,data)
        this_recipe=cls(result[0])
        user_data = {
            **result[0],
            'id':result[0]['users.id'],
            'created_at':result[0]["users.created_at"],
            'updated_at':result[0]['users.updated_at']
        }
        this_user=user_model.User(user_data)
        this_recipe.creator=this_user
        return this_recipe

    @classmethod
    def get_all_recipes(cls):
        query = """
        SELECT * FROM recipes
        JOIN users ON recipes.users_id=users.id;
        """
        recipes_list = connectToMySQL(DATABASE).query_db(query)
        all_recipes = []
        for recipe in recipes_list:
            this_recipe=cls(recipe)
            user_data = {
                **recipe,
                'id':recipe['users.id'],
                'created_at':recipe["users.created_at"],
                'updated_at':recipe['users.updated_at']
            }
            this_user = user_model.User(user_data)
            this_recipe.creator=this_user
            all_recipes.append(this_recipe)
        return all_recipes

    @classmethod
    def add_new_recipe(cls, data):
        query = """
        INSERT INTO recipes (name, description, instructions, under_30_minutes, date_made, users_id) 
        VALUES (%(name)s,%(description)s,%(instructions)s,%(under_30_minutes)s,%(date)s,%(users_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def edit_recipe(cls,data):
        query = """
        UPDATE recipes
        SET name = %(name)s,description=%(description)s,instructions=%(instructions)s,under_30_minutes=%(under_30_minutes)s,date_made=%(date)s,users_id=%(users_id)s
        WHERE id=%(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = """
        DELETE FROM recipes
        WHERE id=%(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def validate(data):
        is_valid = True

        if len(data['name'])<3:
            is_valid = False
            flash("Recipe name must be at least 3 characters")
        
        if len(data['description'])<3:
            is_valid = False
            flash("Recipe description must be at least 3 characters")

        if len(data['instructions'])<3:
            is_valid = False
            flash("Recipe instructions must be at least 3 characters")

        if not data['under_30_minutes']:
            is_valid = False
            flash("Must select if the recipe is under 30 minutes")

        if not data['date']:
            is_valid = False
            flash("Creation date must not be empty")

        return is_valid