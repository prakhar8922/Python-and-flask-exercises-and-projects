# import the User class from a module called 'user'
from user import User

# create a list of user objects
users = [User(1, 'Prakhar', 'password'), User(2, 'Mimi', 'secret')]

# create a dictionary to look up users by username
username_table = {u.username: u for u in users}

# create a dictionary to look up users by user ID
userid_table = {u.id: u for u in users}

# This function takes in a username and password, looks up the corresponding user object from the username_table dictionary, and returns the user object if the password matches. If the username or password is incorrect, the function returns None.


def authenticate(username, password):
    user = username_table.get(username, None)
    if user and password == user.password:
        return user

# This function takes in a JWT payload, extracts the user ID from the payload, and looks up the corresponding user object from the userid_table dictionary. If the user ID is not found, the function returns None.


def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
