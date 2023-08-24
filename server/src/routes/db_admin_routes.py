from flask_restx import Resource

from src import api
from src.lib.db_connection import add_decisions

@api.route('/update_db')
class Search(Resource):
  def post(self):
    add_decisions()
    return 201
