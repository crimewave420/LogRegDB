from broker import Broker
import domain

class Controller():
    def __init__(self):
        self.broker = Broker()
    def add_user(self,User):
        self.broker.add_user(User)      