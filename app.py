from flask import Flask
from flask.ext.restful import Api, Resource
from flask.ext.mysqldb import MySQL
from resources.option import OptionAPI
from resources.user import UserAPI
from resources.food import FoodAPI
from resources.order import OrderAPI
app = Flask(__name__)
api = Api(app)

mysql = MySQL(app)



api.add_resource(UserAPI,'/users/<int:id>', endpoint = 'user')
api.add_resource(FoodAPI,'/api/food', endpoint = 'food')
api.add_resource(OptionAPI,'/api/option/<int:food_id>', endpoint = 'option')
api.add_resource(OrderAPI,'/api/order/<int:order_id>', endpoint = 'order')

if __name__ == '__main__':
	app.run(host='188.166.208.103',debug=True)
