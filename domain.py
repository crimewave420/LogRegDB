class User():
    def __init__(self, username, password, name = None):
        self.username = username
        self.password = password
        self.name = name

    def __str__(self):
        return self.username + " " + self.password
        

class CommitException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return(repr(self.value))    
class QuerryException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return(repr(self.value))    
class UserExistsException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return(repr(self.value))  