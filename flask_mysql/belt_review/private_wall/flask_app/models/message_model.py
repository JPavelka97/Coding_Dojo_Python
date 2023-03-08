from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt
import re

class Message:
    def __init__(self,data):
        self.id=data['id']
        self.sender_id=data['sender_id']
        self.receiver_id=data['receiver_id']
        self.message=data['message']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def new_message(self,data):
        query = """
        INSERT INTO messages (sender_id,receiver_id,message)
        VALUES (%(sender_id)s,%(receiver_id)s,%(message)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_user_messages(self,data):
        query = """
        SELECT * FROM users
        JOIN messages ON users.id = messages.receiver_id
        JOIN users b ON messages.sender_id=b.id
        WHERE receiver_id = 1;
        """
        return connectToMySQL(DATABASE).query_db(query,data)