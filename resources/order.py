import json
from flask_restful import Resource, reqparse
import MySQLdb
class OrderAPI(Resource):
        def __init__(self):
            self.conn = MySQLdb.connect(host="localhost", user = "root", passwd = "Samurai", db = "flint", cursorclass=MySQLdb.cursors.DictCursor)
            self.cur = self.conn.cursor()
	def get(self,order_id):
                self.cur.execute("SELECT * FROM order_details a,options b WHERE a.option_id=b.id and order_id="+str(order_id))
                rv = self.cur.fetchall()
                return json.dumps(rv)
	def post(self,order_id):
                parser = reqparse.RequestParser()
                parser.add_argument('food_id', type=int)
                parser.add_argument('option_id', type=int)
                parser.add_argument('value', type=str)
                args = parser.parse_args()
                args['order_id']=order_id
                insstr = ("INSERT INTO order_details (order_id,food_id,option_id,value) VALUES (%(order_id)s,%(food_id)s,%(option_id)s,%(value)s)")
                try:
                    self.cur.execute(insstr,args)
                    self.conn.commit()
                except:
                    self.conn.rollback()
