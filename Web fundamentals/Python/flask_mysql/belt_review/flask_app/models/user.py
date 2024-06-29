from flask_app.config.mysqlconnection import connectToMySQL , DB

from flask import flash
from flask bcrypt import bcrypt
from flask_app import app
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

bcrypt = Bcrypt(app)

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DB).query_db(query, data)
        if results == ():
            return False
        return cls(results[0])
    
    @classmethod
    def create_user(cls, data):
        encrypted_password = bcrypt.generate_password_hash(data['password'])
        data = dict(data)
        data['password'] = encrypted_password
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        results = connectToMySQL(DB).query_db(query, data)
        return results

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)
        if results == []:
            return []
        return cls(results[0])
    
    @staticmethod
    def validate_register (data):
        is_valid = True
        user_in_db = User.get_by_email(data)
        if len(data['first_name']) < 2:
            is_valid = False
            flash("First name must be at least 2 characters","register")
        if len(data['last_name']) < 2:
            is_valid = False
            flash("Last name must be at least 2 characters","register")
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("Invalid email address","register")
        if user_in_db:
            is_valid = False
            flash("Email already in use","register")
        if len(data['password']) < 8:
            is_valid = False
            flash("Password must be at least 8 characters","register")
        if data['password']!= data['confirm_password']:
            is_valid = False
            flash("Passwords do not match","register")
        return is_valid
    
    @staticmethod
    def validate_login (data):
        is_valid = True
        user_in_db = User.get_by_email(data)
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("Invalid email","login")
        if not user_in_db:
            is_valid = False
            flash("Email not found","login")
        elif not bcrypt.check_password_hash(user_in_db.password, data['password']):
            is_valid = False
            flash("Incorrect password","login")
        return is_valid