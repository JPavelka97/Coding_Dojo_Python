from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_time']
        self.updated_at = data['updated_time']

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('usersdb').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def add_new_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        return connectToMySQL('usersdb').query_db(query, data)

    @classmethod
    def display_single_user(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        result = connectToMySQL('usersdb').query_db(query, data)
        if result:
            return cls(result[0])
        return False

    @classmethod
    def update_user(cls, data):
        query = """UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s WHERE id=%(id)s;"""
        return connectToMySQL('usersdb').query_db(query, data)

    @classmethod
    def delete_user(cls, data):
        query = """DELETE FROM users WHERE id = %(id)s;"""
        return connectToMySQL('usersdb').query_db(query, data)