from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt
import re

bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_by_id(cls, data):
        query = """
        SELECT * FROM users 
        LEFT JOIN recipes ON users.id = recipes.users_id 
        WHERE users.id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_all_users(cls, data):
        query = """
        SELECT * FROM users 
        JOIN recipes ON users.id = recipes.users_id;
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO users (first_name, last_name, email, password)
            VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s)
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate(data):
        is_valid = True

        if len(data["first_name"]) < 2:
            is_valid = False
            flash("First Name must be at least 2 characters.")

        if len(data["last_name"]) < 2:
            is_valid = False
            flash("Last Name must be at least 2 characters.")

        if not EMAIL_REGEX.match(data["email"]):
            is_valid = False
            flash("Invalid email address")

        if len(data["password"]) < 1:
            is_valid = False
            flash("Password cannot be empty.")
        elif not data["confirm_password"] == data["password"]:
            is_valid = False
            flash("Passwords do not match.")

        return is_valid
