import domain
import pyodbc
from helpers import *

class Broker():
    def __init__(self):
        self.connection = pyodbc.connect('DSN=newdsn;Trusted_Connection=yes;', autocommit=True)
        self.cursor = self.connection.cursor()

    def find_user(self,someuser):
        user = None
        try:
            query = "select * from Users where username = '"+ someuser.username + "' and password = '" + someuser.password + "' ;"
            user = self.cursor.execute(query).fetchone()
            
        except:
            raise domain.QuerryException("Failed query")
        finally:
            self.connection.close()
            return user

    def add_user(self, User):
        if user_exists(self.find_user(User)):
            query = "insert into Users values ('{username}','{password}','');".format(username=User.username,password=User.password)
            try:
                self.cursor.execute(query)
                self.cursor.commit()
            except:
                raise domain.CommitException("Failed commit")
            finally:
                self.connection.close()

            

