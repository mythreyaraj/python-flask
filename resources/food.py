import json
from flask_restful import Resource, reqparse
import MySQLdb
class FoodAPI(Resource):
        def __init__(self):
            self.conn = MySQLdb.connect(host="localhost", user = "root", passwd = "Samurai", db = "flint", cursorclass=MySQLdb.cursors.DictCursor)
            self.cur = self.conn.cursor()
	def get(self):
                self.cur.execute('''SELECT id, name, price FROM food''')
                rv = self.cur.fetchall()
                return json.dumps(rv)
	def post(self):
                parser = reqparse.RequestParser()
                parser.add_argument('name', type=str)
                parser.add_argument('price', type=int)
                args = parser.parse_args()
                insstr = ("INSERT INTO food (name,price) VALUES (%(name)s,%(price)s)")
                try:
                    self.cur.execute(insstr,args)
                    self.conn.commit()
                except:
                    self.conn.rollback()
