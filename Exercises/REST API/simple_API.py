# Import the necessary modules
from flask import Flask
from flask_restful import Resource, Api

# Create a Flask application instance
app = Flask(__name__)

# Create an instance of the Flask-RESTful API class
api = Api(app)

# Define a resource class that inherits from Flask-RESTful's Resource class


class HelloWorld(Resource):

    # Define a GET method that returns a simple dictionary
    def get(self):
        return {'hello': 'world'}


# Add the HelloWorld resource to the API with the URL endpoint '/'
api.add_resource(HelloWorld, '/')

# If the module is run directly (not imported as a library), start the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
