# user object for adding new user


# first make the password
class password:
    def __init__(self, salt, hash):
        self.salt = salt
        self.hash = hash


# after that password is made, make user
class newUser:

    # default constructor
    def __init__(self, _id, name, password):
        self._id = _id
        self.name = name
        self.password = password
