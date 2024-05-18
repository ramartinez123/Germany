from flask import Flask
from flask_mysqldb import MySQL
from config.database import *
from flask_login import LoginManager

app=Flask(__name__)
app.config['MYSQL_HOST']= host
app.config['MYSQL_USER']= user
app.config['MYSQL_DB']= database    
app.config['SECRET_KEY'] = 'aaaa'

mysql=MySQL(app)
login_manager = LoginManager(app)

from controller.countryController import *
from controller.stateController import *
from controller.populationController import *
from controller.unemploymentController import *
from controller.indexController import *
from controller.loginController import *
from controller.mapController import *
from models.errors import *
from models.user import users

if __name__ == '__main__':
    app.run(port = 3002, debug = True)