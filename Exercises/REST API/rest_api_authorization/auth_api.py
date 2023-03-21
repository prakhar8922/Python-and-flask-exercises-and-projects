
from flask import Flask
from flask_restful import Resource, Api
from secure_check import authenticate, identity
from flask_jwt import JWT, jwt_required

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

api = Api(app)

# app: The Flask application instance to use for JWT authentication.
jwt = JWT(app, authenticate, identity)
# authenticate: A function that takes in a username and password and returns a user object if the credentials are valid. If the credentials are not valid, the function should return None.
# identity: A function that takes in a payload (a dictionary containing information about the user) and returns a user object. This function is used to retrieve a user object from the database or other data source based on the user's ID.

puppies = []


class PuppyNames(Resource):
    def get(self, name):
        for pup in puppies:
            if pup['name'] == name:
                return pup
        return {'name': None}, 404

    def post(self, name):
        pup = {'name': name}
        puppies.append(pup)

        return pup

    def delete(self, name):

        # Cycle through list for puppies
        for ind, pup in enumerate(puppies):
            if pup['name'] == name:
                # don't really need to save this
                delted_pup = puppies.pop(ind)
                return {'note': 'delete successful'}


class AllNames(Resource):
    @jwt_required()
    def get(self):
        return {'puppies': puppies}


api.add_resource(PuppyNames, '/puppy/<string:name>')
api.add_resource(AllNames, '/puppies')


if __name__ == '__main__':
    app.run(debug=True)
