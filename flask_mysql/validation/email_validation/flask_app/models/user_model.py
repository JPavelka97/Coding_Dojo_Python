from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email_address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        email_results = connectToMySQL('email_db').query_db(query)
        emails = []
        if email_results:
            for email in email_results:
                emails.append(cls(email))
            return emails

    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO emails (email_address) VALUES (%(email)s)
        """
        return connectToMySQL('email_db').query_db(query,data)

    @staticmethod
    def validate_user(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!", 'email')
            is_valid = False
        return is_valid