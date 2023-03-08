from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Form:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, form):
        query = "INSERT INTO dojo_surevy (name, location, language, comment) VALUES (%(name)s,%(location)s,%(language)s,%(comment)s)"
        return connectToMySQL('survey').query_db(query,form)

    @classmethod
    def get_last_form(cls,id):
        query = "SELECT * FROM dojo_survey WHERE id=%(id)s"
        return connectToMySQL('survey').query_db(query,id)

    @staticmethod
    def validate_form(form):
        is_valid = True
        if len(form['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if not form['location']:
            flash("Must choose a location.")
            is_valid = False        
        if not form['language']:
            flash("Must choose a language.")
        if not form['comment']:
            flash("Comment must exist.")
