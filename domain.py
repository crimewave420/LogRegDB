class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_string(self):
        return self.username + " " + self.password
        