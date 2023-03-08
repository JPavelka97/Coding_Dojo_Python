from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app import app
from flask import session
# import models you needs
from flask import flash
from flask_bcrypt import Bcrypt
import re

class Spell:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.desc = data['description']
        self.higher_level = data['higher_level']
        self.range = data['spell_range']
        self.components = data['components']
        self.material = data['material']
        self.ritual = data['ritual']
        self.duration = data['duration']
        self.concentration = data['concentration']
        self.casting_time = data['casting_time']
        self.level = data['level']
        self.level_int = data['level_int']
        self.school = data['school']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def insert_spell_into_db(cls,data):
        query = """
        INSERT INTO spells (name, description, higher_level, spell_range,
        components,material,ritual,duration,concentration,
        casting_time, level,level_int,school)
        VALUES (%(name)s,%(description)s,%(higher_level)s,%(range)s,%(components)s,%(material)s,%(ritual)s,%(duration)s,%(concentration)s,%(casting_time)s,%(level)s,%(level_int)s,%(school)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)


    @classmethod
    def delete_single_spell_from_spellbook(cls,data):
        query = """
        DELETE FROM spellbooks_has_spells
        WHERE spellbook_id = %(spellbook_id)s AND spell_id = %(spell_id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def delete_all_spells_from_spellbook(cls,data):
        query = """
        DELETE FROM spellbooks_has_spells
        WHERE spellbook_id = %(spellbook_id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def link_spell_to_spellbook(cls,data):
        query = """
        INSERT INTO spellbooks_has_spells (spellbook_id,spell_id)
        VALUES (%(spellbook_id)s,%(spell_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_spell_information(cls,data):
        query = """
        SELECT * FROM spells 
        JOIN spellbooks_has_spells ON spell_id = spells.id
        WHERE spellbook_id = %(spellbook_id)s
        AND spells.level = %(spell_level)s
        ORDER BY name ASC;
        """
        list_of_spells = []
        results = connectToMySQL(DATABASE).query_db(query,data)
        for spell in results:
            list_of_spells.append(cls(spell))
        print(list_of_spells)
        return list_of_spells


