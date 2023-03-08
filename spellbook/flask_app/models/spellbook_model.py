from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt
import re

class Spellbook:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.wielder_name = data['wielder_name']
        self.wielder_class = data['wielder_class']
        self.wielder_level = data['wielder_level']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_spellbook(cls,data):
        query = """
        INSERT INTO spellbooks (name,wielder_name,wielder_class,wielder_level,user_id)
        VALUES (%(name)s,%(wielder_name)s,%(wielder_class)s,%(wielder_level)s,%(user_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def delete_spellbook(cls,data):
        query = """
        DELETE FROM spellbooks
        WHERE id=%(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all_by_id(cls,data):
        query = """
        SELECT * FROM spellbooks
        WHERE spellbooks.user_id = %(id)s;
        """
        all_spellbooks = []
        spellbooks_list = connectToMySQL(DATABASE).query_db(query,data)
        for spellbook in spellbooks_list:
            each_spellbook = cls(spellbook)
            all_spellbooks.append(each_spellbook)
        print(all_spellbooks)
        return all_spellbooks
    
    @classmethod
    def get_one_by_id(cls,data):
        query = """
        SELECT * FROM spellbooks
        JOIN users ON spellbooks.user_id = users.id
        WHERE spellbooks.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        spellbook = results[0]
        print(spellbook)
        return spellbook
    
    @staticmethod
    def validate_spellbook(data):
        is_valid = True

        if len(data['spellbook_name']) < 1:
            is_valid = False
            flash("Please name your spellbook", 'creator')

        if len(data['wielder_name']) < 1:
            is_valid = False
            flash("Please enter a wielder", 'creator')

        return is_valid