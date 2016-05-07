from flask_restful import Resource, reqparse
import MySQLdb
import json
class OptionAPI(Resource):
	def __init__(self):
            self.conn = MySQLdb.connect(host="localhost", user = "root", passwd = "Samurai", db = "flint", cursorclass=MySQLdb.cursors.DictCursor)
            self.cur = self.conn.cursor()
        def get(self,food_id):
		selstr = ("SELECT * FROM options WHERE food_id="+str(food_id));
		self.cur.execute(selstr)
		rv = self.cur.fetchall()
		return json.dumps(rv)
        def post(self,food_id):
                parser = reqparse.RequestParser()
                parser.add_argument('name', type=str)
                parser.add_argument('type', type=int)
                parser.add_argument('min', type=float)
                parser.add_argument('max', type=float)
                parser.add_argument('options', type=str)
                parser.add_argument('options_price', type=str)
                parser.add_argument('price', type=float)
                parser.add_argument('parent_id', type=int)
                parser.add_argument('parent_bool', type=bool)
                args = parser.parse_args()
		args['food_id'] = food_id
                insstr = ("INSERT INTO options (food_id,name,type,min,max,options,options_price,price,parent_id,parent_bool) VALUES \
		          (%(food_id)s,%(name)s,%(type)s,%(min)s,%(max)s,%(options)s,%(options_price)s,%(price)s,%(parent_id)s,%(parent_bool)s)")
		try:
			self.cur.execute(insstr,args)
        		self.conn.commit()
		except:
			self.conn.rollback()
