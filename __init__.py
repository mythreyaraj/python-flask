from flask import Flask
from flask.ext.restful import Api, Resource
from resources.food import FoodAPI
from resources.option import OptionAPI
from resources.user import UserAPI
from flask.ext.mysqldb import MySQL

app = Flask(__name__)
api = Api(app)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'flint'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

~                                                                                                                                                                                                                   
~                                                                                                                                                                                                                   
~                                                                                                                                                                                                                   
~                                                                                                                                                                                                                   
~                                                                                                                                                                                                                   
~                                                                                                                                                                                                                   
~                                                                                                                                                                                                                   
~                                                                                                                                                                                                                   
~                                                                                                                                                                                                                   
~                                                                                                                                                                                                                   
~                                                                                                                                                                                                                   
~                                                                                                                                                                                                                   
~                                                                                                                                                                                                                   
~                                                                                                                                                                                                                   
~                                                                                                                                                                                                                   
~                                                                                    
