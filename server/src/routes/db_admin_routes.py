from flask_restx import Resource

from src import api
from src.lib.db_connection import db_connection

@api.route('/update_db')
class UpdateDB(Resource):
  def post(self):
    db_connection.add_decisions()
    return 'Database updated.', 201
