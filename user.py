from mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id = data['id']
        self.user_name = data['user_name']
        self .email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"

        results = connectToMySQL('user_names').query_db(query)

        users = []

        for user in results:
            users.append(cls(user))
        return users

# CREATE
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (user_name, email, created_at, updated_at) VALUES ( %(user_name)s, %(email)s, NOW(), NOW());"

        return connectToMySQL('user_names').query_db(query, data)

# READ
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('user_names').query_db(query, data)
        return cls(result[0])

# UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET user_name=%(user_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('user_names').query_db(query, data)

# DELETE
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('user_names').query_db(query, data)
