from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        dojo_results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        if dojo_results:
            for dojo in dojo_results:
                dojos.append(cls(dojo))
            return dojos
        return False

    @classmethod
    def get_single_dojo(cls,dojo_data):
        query = "SELECT * FROM dojos WHERE id=%(id)s"
        dojo_result = connectToMySQL('dojos_and_ninjas').query_db(query,dojo_data)
        if dojo_result:
            return cls(dojo_result[0])
        return False

    @classmethod
    def retrieve_all_ninjas_in_dojo(cls,dojo_data):
        query = """
        SELECT * FROM dojos LEFT JOIN ninjas 
        ON ninjas.dojo_id = dojos.id 
        WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL('dojos_and_ninjas').query_db(query,dojo_data)
        dojo = cls(results[0])
        list_of_ninjas = []
        for one_ninja in results:
            ninja_data = {
                "id":one_ninja["ninjas.id"],
                "first_name":one_ninja["first_name"],
                "last_name":one_ninja["last_name"],
                "age":one_ninja["age"],
                "dojo_id":one_ninja["dojo_id"],
                "created_at":one_ninja["ninjas.created_at"],
                "updated_at":one_ninja["ninjas.updated_at"]
            }
            list_of_ninjas.append(ninja.Ninja(ninja_data))
        dojo.ninjas = list_of_ninjas
        return dojo

    @classmethod
    def add_new_dojo(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)
    
