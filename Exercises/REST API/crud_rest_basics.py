
from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)

api = Api(app)

puppies = []


# define a resource for puppy names
class PuppyNames(Resource):

    # GET method to retrieve a specific puppy by name
    def get(self, name):
        for pup in puppies:
            if pup['name'] == name:
                return pup
        return {'name': None}, 404

    # POST method to add a new puppy to the list
    def post(self, name):
        pup = {'name': name}
        puppies.append(pup)
        return pup

    # DELETE method to remove a specific puppy by name
    def delete(self, name):
        for ind, pup in enumerate(puppies):
            if pup['name'] == name:
                delted_pup = puppies.pop(ind)
                return {'note': 'delete successful'}


class AllNames(Resource):
    def get(self):
        return {'puppies': puppies}


api.add_resource(PuppyNames, '/puppy/<string:name>')
api.add_resource(AllNames, '/puppies')


if __name__ == '__main__':
    app.run(debug=True)
