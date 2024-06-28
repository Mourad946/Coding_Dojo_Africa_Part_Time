from flask_app.config.mysqlconnection import connectToMySQL , DB
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results= connectToMySQL(DB).query_db(query) 
        if results == []:
            return []
        result = []
        for dojo in results:
            result.append(cls(dojo))
        return result


    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def get_ninjafrom(cls, data):
        query = "select * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id where dojos.id = %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)
        if results == []:
            return []
        dojo = cls(results[0])
        for i in results:
            n = {
                'id': i['ninjas.id'],
                'firstname': i['firstname'],
                'lastname': i['lastname'],
                'age': i['age'],
                'created_at': i['ninjas.created_at'],
                'updated_at': i['ninjas.updated_at'],
            }
            dojo.ninjas.append( Ninja(n)) 
        return dojo