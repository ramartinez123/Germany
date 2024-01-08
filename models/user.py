from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import *

class User(UserMixin):
    def __init__(self, id, name, password, is_admin=False):
        self.id = id
        self.name = name 
        self.password = password
        self.is_admin = is_admin

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

names=User(1,"Juan","12344",True)
names.set_password("1234")

users = []
users.append(names)

def get_user(names):
    for user in users:
        if user.name == names:
            return user
    return None

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id ==int(user_id):
          return user
    return None 
